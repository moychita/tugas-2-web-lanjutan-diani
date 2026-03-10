from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    deskripsi = Column(String, nullable=True)
    kategori = Column(String, nullable=True)