from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Creatives Management System Backend is Running!"}
