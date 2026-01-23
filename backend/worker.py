from celery import Celery
import subprocess

celery = Celery(
    "genomeflow",
    broker="redis://redis:6379/0"
)

@celery.task
def run_fastqc(file_path: str):
    cmd = ["fastqc", file_path, "-o", "/tmp/qc"]
    subprocess.run(cmd, check=True)
    return "QC completed"
