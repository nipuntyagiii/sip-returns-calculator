from app.calculator import calculate_sip
from app.utils import validate_inputs

def main():
    try:
        monthly = float(input("Enter monthly SIP amount: "))
        rate = float(input("Enter expected annual return (%): "))
        years = int(input("Enter investment duration (years): "))

        validate_inputs(monthly, rate, years)
        result = calculate_sip(monthly, rate, years)

        print("\n--- SIP Investment Summary ---")
        print(f"Monthly Investment: ₹{result['monthly_investment']}")
        print(f"Duration: {result['years']} years")
        print(f"Annual Return Rate: {result['annual_rate']}%")
        print(f"Total Invested: ₹{result['total_invested']}")
        print(f"Future Value: ₹{result['future_value']}")
        print(f"Absolute Return: ₹{result['absolute_return']}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
