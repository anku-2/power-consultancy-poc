from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/materials")
def add_material(material: schemas.MaterialCreate, db: Session = Depends(get_db)):
    m = models.Material(**material.dict())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@app.get("/materials")
def list_materials(db: Session = Depends(get_db)):
    return db.query(models.Material).all()
