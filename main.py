from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tugas 2 Web Lanjutan")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    data = models.Item(**item.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


@app.get("/items/", response_model=list[schemas.ItemOut])
def get_all_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()


@app.get("/items/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    data = db.query(models.Item).filter(models.Item.id == item_id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Item tidak ditemukan")
    return data