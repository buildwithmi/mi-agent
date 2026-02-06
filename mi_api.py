from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = open("mi_identity.txt").read()

@app.get("/")
def home():
    return {"status": "Mi is alive"}

@app.post("/mi")
def mi(message: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages,
        temperature=0.7
    )

    return {"reply": response.choices[0].message.content}
