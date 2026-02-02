# Power Consultancy Web App (POC)

## Overview
This project is a small Proof of Concept (POC) web application for a power consultancy use case.
It demonstrates material tracking and a simple procurement flow with bilingual support
(English and Chinese).

The purpose of this POC is to showcase architecture, code structure, and development approach.

---

## Tech Stack Used

### Frontend
- React JS
- Axios
- react-i18next (for language support)

### Backend
- Python (FastAPI)
- SQLAlchemy ORM

### Database
- MySQL

### Tools
- VS Code
- Node.js
- Python Virtual Environment

---

## Features
- Basic login-ready structure (POC level)
- Material tracking (add & view materials)
- Simple procurement status flow
- Bilingual support (English & Chinese)
- REST API-based communication

---

## How to Run the Project

### Backend
```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
Backend runs at:
http://127.0.0.1:8000/docs

Frontend
cd frontend
npm install
npm start
Frontend runs at:
http://localhost:3000
