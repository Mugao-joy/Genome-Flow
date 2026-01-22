from fastapi import FastAPI

app = FastAPI(title="GenomeFlow")

@app.get("/")
def health():
    return {"status": "GenomeFlow running"}
