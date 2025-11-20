# 🚀 AI-Powered Article Insight Engine

Convert any article URL into AI-generated summaries and insights, delivered directly to your email — fully automated using **FastAPI + n8n + OpenAI**.

## 🎥 Demo Video (Google Drive)
Adjusting the resolution is recommended for the best experience.

[![Watch the video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://drive.google.com/file/d/1XdZJz5jcFpWXscVf7tK27P2xZzOlRD9u/view?usp=sharing)


---

## 📌 Features

### 🔹 Smart Article Processing
- Extracts content from any URL  
- Summarizes using GPT-based models  
- Generates structured insights for better understanding  

### 🔹 FastAPI Backend
- Clean and simple `/submit-article` endpoint  
- Validates email + article URL  
- Forwards data securely to your n8n workflow  

### 🔹 n8n Workflow Automation
- Fetches article  
- Summarizes via **OpenAI**  
- Extracts insights  
- Saves records to **Google Sheets**  
- Sends summary to user email  

### 🔹 Responsive Frontend UI
- Simple minimal form  
- Clean, modern styling  
- Calls backend using `fetch()`  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| **Backend API** | FastAPI |
| **Automation Engine** | n8n |
| **HTTP Client** | httpx / requests |
| **AI Model** | OpenAI GPT |
| **Frontend** | HTML + CSS + JavaScript |
| **Email Delivery** | Gmail via n8n |

---

## ⚙️ Backend Setup

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
---

2️⃣ Run the FastAPI server

```bash
uvicorn main:app --reload
```

## 🔗 Backend Endpoint
POST /submit-article
Request Body:
{
  "email": "user@example.com",
  "article_url": "https://example.com/article"
}
This forwards the payload to your n8n webhook for automated processing.

-----

## 🔧 Configure Your n8n Webhook

Inside main.py, replace this:
```bash
N8N_WEBHOOK_URL = "YOUR_N8N_WEBHOOK_URL"
```
with your actual webhook URL: "https://your-n8n-server.com/webhook/submit"

-----

##🌐 Frontend Usage

Open: index.html
Enter: Email and Article URL

Click Submit → your backend → n8n → summary email is sent 📩

-----

##📤 Automation Flow (n8n)

Your n8n workflow performs:

🟦 Fetch article content
🟩 Process using OpenAI GPT
🟧 Generate summary + insights
🟨 Save to Google Sheet
🟥 Send Email to User

-----

💙 Support
If this project helps you, give the repo a ⭐ on GitHub!
