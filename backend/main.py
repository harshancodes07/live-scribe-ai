from fastapi import FastAPI, UploadFile , File 
from pydantic import BaseModel
from ai import generate_answer
from transcription import transcribe_audio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
@app.post("/transcribe") 
async def transcribe(file: UploadFile = File(...)):
    contents = await file.read()

    with open(file.filename, "wb") as f:
        f.write(contents)

    transcript = transcribe_audio(file.filename)

    answer = generate_answer(transcript)

    return {
        "filename": file.filename,
        "transcript": transcript,
        "answer" : answer 
    }   
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Livescribe AI "
    }

