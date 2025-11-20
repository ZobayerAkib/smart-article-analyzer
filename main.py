from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid
import httpx
from pydantic import BaseModel, EmailStr

N8N_WEBHOOK_URL = "Add your WEBHOOK URL"

app = FastAPI()

# ----------------------------
# ENABLE CORS (IMPORTANT)
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow all frontend origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ArticleRequest(BaseModel):
    email: EmailStr
    article_url: str

@app.post("/submit-article")
async def submit_article(payload: ArticleRequest):
    session_id = str(uuid.uuid4())

    forward_payload = {
        "email": payload.email,
        "article_url": payload.article_url,
        "session_id": session_id
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(N8N_WEBHOOK_URL, json=forward_payload)

        try:
            data = response.json()
        except:
            data = response.text

        return {
            "status": "success",
            "session_id": session_id,
            "n8n_response": data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
