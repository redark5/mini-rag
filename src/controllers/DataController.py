from .BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # Convert MB to Bytes

    def validate_uploaded_file(self, file: UploadFile):
        # Implement your file validation logic here
        # For example, you can check the file type and size against the settings
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False    #, "File type not allowed."
        if file.size > self.settings.FILE_MAX_SIZE * self.size_scale:
            return False  #, "File size exceeds the maximum limit."
        return True   #, "File is valid."
