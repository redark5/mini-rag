from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, settings
from controllers import DataController

data_router = APIRouter(
prefix="/api/v1/data",
tags=["api_v1", "data"]

)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings: settings = Depends(get_settings)):

# Implement your file upload logic here (validation)
    # For example, you can save the uploaded file to a specific directory
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    #return  { "is_valid": is_valid, "signal": result_signal }


    if not is_valid:
        return JSONResponse(
              status_code=status.HTTP_400_BAD_REQUEST, 
              content={"signal": result_signal
            }
        )
