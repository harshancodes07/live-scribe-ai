from fastapi import FastAPI
from pydantic import BaseModel
from ai import generate_answer

app = FastAPI()

class Question(BaseModel):
    question : str 

@app.get("/")
def home ():
    return {"message" : "Livescribe is running..."}

@app.post("/ask")
def ask_ai(data : Question ):
    answer = generate_answer(data.question)
    return {
        "question" : data.question , 
        "answer" : answer 
    }
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Livescribe AI "
    }

