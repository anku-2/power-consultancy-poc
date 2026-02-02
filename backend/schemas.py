from pydantic import BaseModel

class MaterialCreate(BaseModel):
    name: str
    quantity: int
    project: str
    status: str

class MaterialOut(MaterialCreate):
    id: int
