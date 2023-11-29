from pydantic import BaseModel


class Review(BaseModel):
    title: str
    description: str
    author: str 
    product: str