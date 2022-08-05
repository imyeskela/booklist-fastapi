from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    written_date: str
    description: str


class Book(BookBase):
    id: int
    user_id: int


class BookCreate(BookBase):
    pass