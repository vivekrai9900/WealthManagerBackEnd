import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "portfolio.xlsx"

def normalize(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("₹", "").str.replace("(", "").str.replace(")", "")
    return df

def get_holdings():
    df = pd.read_excel(DATA_PATH, sheet_name="Holdings")
    df = normalize(df)

    holdings = []
    for _, row in df.iterrows():
        value = row["quantity"] * row["current_price"]
        gain_loss = (row["current_price"] - row["avg_price"]) * row["quantity"]
        gain_loss_percent = (gain_loss / (row["avg_price"] * row["quantity"])) * 100

        holdings.append({
            "symbol": row["symbol"],
            "name": row["company_name"],
            "quantity": int(row["quantity"]),
            "avgPrice": row["avg_price"],
            "currentPrice": row["current_price"],
            "sector": row["sector"],
            "marketCap": row["market_cap"],
            "exchange": row["exchange"],
            "value": round(value, 2),
            "gainLoss": round(gain_loss, 2),
            "gainLossPercent": round(gain_loss_percent, 2),
        })

    return holdings

def get_allocation():
    sector_df = pd.read_excel(DATA_PATH, sheet_name="Sector_Allocation")
    market_df = pd.read_excel(DATA_PATH, sheet_name="Market_Cap")
    sector_df = normalize(sector_df)
    market_df = normalize(market_df)

    sector_alloc = {
        row["sector"]: {
            "value": float(str(row["value"]).replace(",", "")),
            "percentage": float(str(row["percentage"]).replace("%", "")),
            "holdingsCount": int(row["holdings_count"])
        }
        for _, row in sector_df.iterrows()
    }

    market_alloc = {
        row["market_cap"]: {
            "value": float(str(row["value"]).replace(",", "")),
            "percentage": float(str(row["percentage"]).replace("%", "")),
            "holdingsCount": int(row["holdings_count"])
        }
        for _, row in market_df.iterrows()
    }

    # ✅ Compute totalValue from sector allocation values
    total_value = sum(item["value"] for item in sector_alloc.values())

    return {
        "bySector": sector_alloc,
        "byMarketCap": market_alloc,
        "totalValue": round(total_value, 2)  # ✅ Add this line
    }


def get_performance():
    df = pd.read_excel(DATA_PATH, sheet_name="Historical_Performance")
    df = normalize(df)

    timeline = [
        {
            "date": row["date"].strftime("%Y-%m-%d"),
            "portfolio": row["portfolio_value"],
            "nifty50": row["nifty_50"],
            "gold": row["gold"]

        }
        for _, row in df.iterrows()
    ]

    def get_return_pct(col):
        latest = df[col].iloc[-1]
        past_1mo = df[col].iloc[-2]
        past_3mo = df[col].iloc[-4]
        past_12mo = df[col].iloc[0]
        return {
            "1month": round((latest - past_1mo) / past_1mo * 100, 2),
            "3months": round((latest - past_3mo) / past_3mo * 100, 2),
            "1year": round((latest - past_12mo) / past_12mo * 100, 2),
        }

    return {
        "timeline": timeline,
        "returns": {
            "portfolio": get_return_pct("portfolio_value"),
            "nifty50": get_return_pct("nifty_50"),
            "gold": get_return_pct("gold")
        }
    }

def get_summary():
    summary_df = pd.read_excel(DATA_PATH, sheet_name="Summary")
    top_df = pd.read_excel(DATA_PATH, sheet_name="Top_Performers")
    holdings_df = pd.read_excel(DATA_PATH, sheet_name="Holdings")
    summary_df = normalize(summary_df)
    top_df = normalize(top_df)
    holdings_df = normalize(holdings_df)

    summary_dict = {row["metric"].lower().replace(" ", "_"): row["value"] for _, row in summary_df.iterrows()}

    best_row = top_df[top_df["metric"] == "Best Performer"].iloc[0]
    worst_row = top_df[top_df["metric"] == "Worst Performer"].iloc[0]

    # ✅ Calculate total holding value
    total_holding_value = sum(holdings_df["quantity"] * holdings_df["current_price"])

    return {
        "totalValue": float(str(summary_dict["total_portfolio_value"]).replace(",", "")),
        "totalInvested": float(str(summary_dict["total_invested_amount"]).replace(",", "")),
        "totalGainLoss": float(str(summary_dict["total_gain/loss"]).replace(",", "")),
        "totalGainLossPercent": float(str(summary_dict["total_gain/loss_%"]).replace("%", "")),
        "totalHolding": round(total_holding_value, 2),  # ✅ Add this
        "topPerformer": {
            "symbol": best_row["symbol"],
            "name": best_row["company_name"],
            "gainPercent": float(str(best_row["performance"]).replace("%", ""))
        },
        "worstPerformer": {
            "symbol": worst_row["symbol"],
            "name": worst_row["company_name"],
            "gainPercent": float(str(worst_row["performance"]).replace("%", ""))
        },
        "diversificationScore": float(str(summary_dict["diversification_score"]).split("/")[0]),
        "riskLevel": summary_dict["risk_level"]
    }

