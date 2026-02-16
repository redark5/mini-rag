from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
# uvicorn main:app --reload --host 0.0.0.0 --port 8000

def welcome():
    return {"message": "Welcome to mini-rag!"}
