from fastapi import FastAPI, HTTPException
from app.calculator import calculate_sip
from app.utils import validate_inputs

app = FastAPI(title="SIP Returns Calculator API")

@app.get("/sip")
def calculate_sip_api(monthly: float, rate: float, years: int):
    try:
        validate_inputs(monthly, rate, years)
        return calculate_sip(monthly, rate, years)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
