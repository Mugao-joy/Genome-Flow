from db import SessionLocal
from models import Sample
from fastapi import FastAPI, UploadFile, File
from storage import upload_file, get_file_url
import uuid

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

@app.post("/upload")
async def upload_genomic_file(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    object_name = f"{file_id}_{file.filename}"

    upload_file(file.file, object_name)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "s3_path": object_name,
        "url": get_file_url(object_name)
    }
