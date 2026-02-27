from enum import Enum

class ResponseSignal(Enum):


    FILE_VALIDATED_SUCCESS = "FILE_VALIDATED_SUCCESS"
    FILE_TYPE_NOT_SUPPORTED = "File type not allowed."
    FILE_SIZE_EXEEDED = "File size exceeds the maximum limit."
    FILE_UPLOAD_SUCCESS = "File is valid."
    FILE_UPLOAD_FAILED = "File is Failed."
    FILE_PROCESSING_FAILED = "File processing failed."
    FILE_PROCESSED_SUCCESS = "File processed successfully."


     