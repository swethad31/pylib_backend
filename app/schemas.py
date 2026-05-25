from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    author: str = Field(min_length=2, max_length=50)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str

    class Config:
        from_attributes = True