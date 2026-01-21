from app.calculator import calculate_sip

def test_basic_sip_calculation():
    result = calculate_sip(1000, 12, 10)
    assert result["total_invested"] == 120000
    assert result["future_value"] > result["total_invested"]
