import os
import json
from datetime import datetime, timedelta

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

import google.generativeai as genai

from tools import DriveSearchTool

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

drive_tool = DriveSearchTool()


class ChatRequest(BaseModel):
    message: str


def build_drive_query_with_ai(user_message: str):
    today = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    last_week = (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")

    prompt = f"""
You are a Google Drive query generator.

Convert the user request into a valid Google Drive API q parameter.

Rules:
- Always include: trashed=false
- PDF: mimeType='application/pdf'
- Folder: mimeType='application/vnd.google-apps.folder'
- Images: mimeType contains 'image/'
- PNG images: mimeType='image/png'
- Video files: mimeType contains 'video/'
- Google Docs: mimeType='application/vnd.google-apps.document'
- Google Sheets: mimeType='application/vnd.google-apps.spreadsheet'
- Name search: name contains 'keyword'
- Content search: fullText contains 'keyword'
- Last week: modifiedTime > '{last_week}'
- Today is: {today}

Important:
- Prefer short single keywords instead of long phrases.
- Do not use plural phrases like name contains 'daily reports'.
- For "daily reports", use: name contains 'Daily'
- For "reports", use: name contains 'Report'
- For "invoices", use: name contains 'invoice' or name contains 'invoices'
- For "qr codes", use: name contains 'qr'
- For "employee sheet", use: name contains 'employees'
- For "shell script" or "setup script", use: name contains 'setup' or name contains 'sh'
- For "all files", use only: trashed=false

Return ONLY valid JSON. No markdown. No explanation.

Examples:

User: find daily reports
{{
  "q": "trashed=false and name contains 'Daily'"
}}

User: find pdf files
{{
  "q": "trashed=false and mimeType='application/pdf'"
}}

User: find image files
{{
  "q": "trashed=false and mimeType contains 'image/'"
}}

User: find qr codes
{{
  "q": "trashed=false and name contains 'qr'"
}}

User: show folders
{{
  "q": "trashed=false and mimeType='application/vnd.google-apps.folder'"
}}

User request:
{user_message}
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    try:
        text = text.replace("```json", "").replace("```", "").strip()
        data = json.loads(text)
        return data.get("q", "trashed=false")
    except Exception:
        return "trashed=false"


@app.post("/chat")
def chat(request: ChatRequest):
    q = build_drive_query_with_ai(request.message)

    files = drive_tool.run(q)

    if not files:
        return {
            "reply": "No matching files found. Try a simpler keyword like 'Daily', 'invoice', 'qr', or 'pdf'.",
            "query_used": q,
            "files": []
        }

    return {
        "reply": f"I found {len(files)} matching file(s).",
        "query_used": q,
        "files": files
    }


@app.get("/")
def home():
    return {
        "message": "Google Drive AI Agent Backend is running."
    }