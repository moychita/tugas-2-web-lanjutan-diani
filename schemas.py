from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    nama: str
    deskripsi: Optional[str] = None
    kategori: Optional[str] = None

class ItemOut(ItemCreate):
    id: int

    class Config:
        orm_atribute = True