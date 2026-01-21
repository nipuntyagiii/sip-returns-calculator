def calculate_sip(monthly_investment: float, annual_rate: float, years: int) -> dict:
    months = years * 12
    monthly_rate = annual_rate / 12 / 100

    future_value = monthly_investment * (
        ((1 + monthly_rate) ** months - 1) / monthly_rate
    ) * (1 + monthly_rate)

    total_invested = monthly_investment * months
    absolute_return = future_value - total_invested

    return {
        "monthly_investment": monthly_investment,
        "years": years,
        "annual_rate": annual_rate,
        "total_invested": round(total_invested, 2),
        "future_value": round(future_value, 2),
        "absolute_return": round(absolute_return, 2),
    }
