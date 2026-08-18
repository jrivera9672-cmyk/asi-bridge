from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

ASI_API_KEY = os.getenv("ASI_API_KEY")
ASI_ENDPOINT = "https://api.asi1.ai/v1/chat/completions"

@app.get("/")
def home():
    return {"status": "ASI Bridge Online"}

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt", "")

    headers = {
        "Authorization": f"Bearer {ASI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "asi1",
        "messages": [{"role": "user", "content": user_prompt}]
    }

    response = requests.post(ASI_ENDPOINT, json=payload, headers=headers)
    return response.json()
