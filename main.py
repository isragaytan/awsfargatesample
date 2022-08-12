from fastapi import FastAPI

# PYTHON python3 -m uvicorn main:app --reload

app = FastAPI()

@app.get('/')
def index():
    return "Hello world again and again"