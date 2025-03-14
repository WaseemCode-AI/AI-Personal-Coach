from fastapi import FastAPI
from chatbot import chat_with_ai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI Personal Coach"}

@app.get("/ask/{query}")
def ask_ai(query: str):
    return {"response": chat_with_ai(query)}
