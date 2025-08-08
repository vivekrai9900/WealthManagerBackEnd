# WealthManagerBackEnd
# 📊 WealthManager.online – Portfolio Analytics Dashboard

A full-stack application that provides Indian investors with a clear, comprehensive view of their investment portfolios. Designed as part of a full-stack developer intern assignment for WealthManager.online.

---

## 🚀 Features

### ✅ Backend
- RESTful API built for portfolio analytics
- Key endpoints:
  - `/api/portfolio/holdings`
  - `/api/portfolio/allocation`
  - `/api/portfolio/performance`
  - `/api/portfolio/summary`
- Realistic data modeling for:
  - Holdings
  - Sector and market cap allocation
  - Benchmark comparisons (vs Nifty50 & Gold)
- Robust error handling and input validation

### 🎯 Frontend
- Interactive React (or your framework) dashboard
- Mobile-friendly responsive design
- Key sections:
  - Portfolio overview cards
  - Sector & market cap pie charts
  - Performance comparison line chart
  - Sortable/searchable holdings table
  - Top/worst performers section

---

## ⚙️ Tech Stack

| Layer     | Tech Used                 |
|-----------|---------------------------|
| Frontend  | React.js, Chart.js/Recharts, CSS/Tailwind |
| Backend   | FastAPI / Node.js / Express |
| Data Store| Static JSON / Excel converted |
| Deployment| Vercel / Render / Netlify / Railway / Replit |

---

## 📂 API Endpoints

### 1. GET `/api/portfolio/holdings`
Returns detailed holdings with calculated values and gain/loss.

### 2. GET `/api/portfolio/allocation`
Returns asset allocation by **sector** and **market cap**.

### 3. GET `/api/portfolio/performance`
Returns performance timeline and benchmark comparison (Nifty50, Gold).

### 4. GET `/api/portfolio/summary`
Returns key insights: total value, top/worst performer, risk level, etc.

---

## 📈 Sample Screenshots

*(Include screenshots or GIFs of each section if available)*

---

## 🧠 AI Tools Used

| Tool        | Use Case |
|-------------|----------|
| ChatGPT     | Generating sample JSON data, error messages, README.md |
| GitHub Copilot | Refactoring frontend components & chart code |

> Code was written manually with AI assistance for speed and structure refinement. All logic and data processing was hand-authored and verified.

---

## ✅ Working Demo

- 🔗 Live Frontend: [your-frontend-url]
- 🔗 Live API: [your-backend-url]
- 📁 Sample Data: [Google Sheet](https://docs.google.com/spreadsheets/d/e/2PACX-1vTEIflXcZ6X-gxHOExxEbZq_i-UscM6HfsZj5tog9pkw6PQfi6E5u4NRRNuKpWTUSfufqkvDjP32NJD/pub?output=xlsx)

---

## 📦 Local Setup

```bash
# Clone the repo
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/vivekrai9900/WealthManagerBackEnd.git)
cd your-repo-name

# Backend
cd backend
pip install -r requirements.txt 
uvicorn main:app --reload       

# Frontend
cd frontend
yarn install
yarn dev
