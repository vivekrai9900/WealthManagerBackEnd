from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils import get_holdings, get_allocation, get_performance, get_summary

app = FastAPI(title="WealthManager Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/portfolio/holdings")
def portfolio_holdings():
    return get_holdings()

@app.get("/api/portfolio/allocation")
def portfolio_allocation():
    return get_allocation()

@app.get("/api/portfolio/performance")
def portfolio_performance():
    return get_performance()

@app.get("/api/portfolio/summary")
def portfolio_summary():
    return get_summary()
