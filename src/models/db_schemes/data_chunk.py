from pydantic import BaseModel, Field, validator
from bson.objectid import ObjectId
from typing import Optional


class DataChunk(BaseModel):
    """DataChunk model to represent a chunk of data in the database."""
    _id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict 
    chunk_order: int= Field(..., ge=0)  # Ensure chunk_order is a non-negative integer
    chunk_project_id: ObjectId


  

    class Config:
        """Configuration for the DataChunk model."""
        arbitrary_types_allowed = True