from fastapi import FastAPI
from config import Settings

app = FastAPI(title = Settings.TITLE, version = Settings.VERSION)

@app.get("/")
def hello():
    return {"msg":"Hello FastAPI"}