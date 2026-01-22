from fastapi import FastAPI
from db import SessionLocal
from models import Sample

app = FastAPI(title="GenomeFlow")

@app.post("/samples")
def create_sample(external_id: str, organism: str, tissue: str):
    db = SessionLocal()
    sample = Sample(
        external_id=external_id,
        organism=organism,
        tissue=tissue
    )
    db.add(sample)
    db.commit()
    db.refresh(sample)
    return sample
