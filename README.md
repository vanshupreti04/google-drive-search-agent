# 🔎 DriveMind AI

<img width="932" height="321" alt="image" src="https://github.com/user-attachments/assets/fe0f1359-e8da-459a-b35e-0367e498b29e" />


<div align="center">

### Conversational AI Agent for Google Drive File Discovery

Search, filter, and discover Google Drive files using natural language powered by Gemini AI, FastAPI, and Streamlit.

<br/>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white" />
<img src="https://img.shields.io/badge/Google_Drive_API-34A853?style=for-the-badge&logo=googledrive&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge" />

<br/>
<br/>

</div>

---

# ✨ Features

✅ Conversational AI-powered Google Drive search
✅ Search files using natural language
✅ Search by file name, type, content, and modified date
✅ Google Drive API integration using Service Account
✅ Gemini AI powered query understanding
✅ FastAPI backend architecture
✅ Streamlit interactive chat UI
✅ AI-generated Google Drive query generation
✅ Supports PDFs, images, folders, spreadsheets, docs, videos, and more
✅ Clean responsive UI for file discovery

---

# 🧠 How It Works

```text
User Query
     ↓
Gemini AI understands intent
     ↓
Generates Google Drive q parameter
     ↓
Google Drive API searches files
     ↓
FastAPI returns results
     ↓
Streamlit displays matching files
```

---

# 🏗️ Project Architecture

```text
DriveMind AI
│
├── backend/
│   ├── main.py
│   ├── drive_service.py
│   ├── tools.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

---

# 🛠️ Tech Stack

| Technology          | Purpose                        |
| ------------------- | ------------------------------ |
| 🐍 Python           | Core Programming Language      |
| ⚡ FastAPI           | Backend API Framework          |
| 🎨 Streamlit        | Frontend Chat Interface        |
| 🤖 Gemini AI        | Natural Language Understanding |
| ☁️ Google Drive API | File Discovery & Search        |
| 🔗 LangChain        | Tool-based AI Integration      |

---

# 🌐 Live Demo

### 🚀 Frontend (Streamlit App)

[🔗 Open DriveMind AI Frontend](https://drivemind-frontend.onrender.com)

### ⚡ Backend API

[🔗 Open FastAPI Backend](https://drivemind-backend.onrender.com)

---

# 🔍 Supported Searches

The AI agent supports:

### 📄 File Type Search

```text
find pdf files
find image files
show folders
find spreadsheets
```

### 🧩 Name-Based Search

```text
find daily reports
find qr codes
find invoices
find employee sheet
```

### 📅 Date-Based Search

```text
find files modified last week
find recent reports
```

### 💬 Conversational Queries

```text
find networking certificate
show all reports
find project requirements pdf
```

---

# 🤖 AI Query Generation Example

### User Input

```text
find daily reports
```

### Gemini Generated Drive Query

```text
trashed=false and name contains 'Daily'
```

### Google Drive API Search

```python
service.files().list(q=q)
```

---

# 📸 Application Preview

## 🔹 Conversational Search UI

<img width="1906" height="846" alt="image" src="https://github.com/user-attachments/assets/fb47e530-750f-4e64-9f20-265c51651879" />


---

# 🚀 Local Setup

## 1️⃣ Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd drive-ai-agent
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Add your:

```text
service_account.json
```

Run backend:

```bash
uvicorn main:app --reload
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

# 🔐 Google Drive API Setup

1. Enable Google Drive API from Google Cloud Console
2. Create Service Account
3. Download JSON credentials
4. Share Google Drive folder with service account email
5. Add `service_account.json` inside backend folder

---

# 🌐 Deployment

## Backend Deployment

Deploy FastAPI backend on:

* Render
* Railway
* Fly.io

### Backend Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## Frontend Deployment

Deploy Streamlit frontend on:

* Streamlit Cloud
* Render

---

# 📂 Example Test Files

```text
financial_report_2024.pdf
marketing_strategy.pdf
budget_sheet.xlsx
invoice_march.pdf
computer_networking_certificate.pdf
project_requirements.pdf
```

---

# 💡 Key Highlights

✔ AI-generated Google Drive search queries
✔ Real-time conversational file discovery
✔ Modular FastAPI architecture
✔ Service Account authentication
✔ Streamlit interactive UI
✔ Professional deployment-ready structure

---

