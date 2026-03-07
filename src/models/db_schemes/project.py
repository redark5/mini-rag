from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId


class Project(BaseModel):
    """Project model to represent a project in the database."""
    id: Optional[ObjectId] = Field(None, alias='_id') 
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value):
        """Validator to ensure project_id is not empty."""
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value


    class Config:
        """Configuration for the Project model."""
        arbitrary_types_allowed = True
        populate_by_name = True
    