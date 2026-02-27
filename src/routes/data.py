from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignal

import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
prefix="/api/v1/data",
tags=["api_v1", "data"]

)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings: settings = Depends(get_settings)):

    data_controller = DataController()
# Implement your file upload logic here (validation)
    # For example, you can save the uploaded file to a specific directory
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    #return  { "is_valid": is_valid, "signal": result_signal }


    if not is_valid:
        return JSONResponse(
              status_code=status.HTTP_400_BAD_REQUEST, 
              content={"signal": result_signal
            }
        )
        #logger.warning(f"File validation failed: {result_signal}")

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path , file_id = data_controller.generate_Unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"signal": ResponseSignal.FILE_UPLOAD_FAILED.value, "error": str(e)}
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value, "file_id": file_id}
    )