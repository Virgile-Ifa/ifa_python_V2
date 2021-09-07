from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def read_root():
    return {"Test: l'API est fonctionelle"}

@app.get("/test/generateur")
def read_root():
    return {}

