from db import SessionLocal
from models import Sample
from fastapi import FastAPI, UploadFile, File
from storage import upload_file, get_file_url
import uuid
from worker import run_fastqc

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



@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    object_name = f"{file_id}_{file.filename}"

    upload_file(file.file, object_name)
    run_fastqc.delay(object_name)

    return {
        "status": "uploaded",
        "qc": "started",
        "object": object_name
    }