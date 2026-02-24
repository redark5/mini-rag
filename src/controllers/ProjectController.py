from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()
    
    def get_project_path(self, project_id: str):
        # Implement logic to get the project path based on the project_id
        # For example, you can construct the path using a base directory and the project_id
        project_dir = os.path.join(
            self.files_dir, project_id
        )

        # Ensure the project directory exists
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)    
        return project_dir