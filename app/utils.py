def validate_inputs(monthly_investment, annual_rate, years):
    if monthly_investment <= 0:
        raise ValueError("Monthly investment must be greater than 0")
    if annual_rate <= 0:
        raise ValueError("Annual rate must be greater than 0")
    if years <= 0:
        raise ValueError("Investment duration must be greater than 0")
