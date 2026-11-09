import math

# Finance Calculator: Investment & Home Loan Repayment
calculation_type = input("Enter 'investment' or 'bond' from the menu: ").strip().lower()

if calculation_type == "investment":
    deposit = float(input("Enter deposit amount: "))
    rate = float(input("Enter interest rate (%): ")) / 100
    years = float(input("Enter number of years: "))
    interest = input("Enter 'simple' or 'compound' interest: ").strip().lower()

    if interest == "simple":
        total = deposit * (1 + rate * years)
    else:
        total = deposit * math.pow((1 + rate), years)

    print(f"Total return: R{total:.2f}")

elif calculation_type == "bond":
    house_value = float(input("Enter present value of the house: "))
    rate = (float(input("Enter annual interest rate (%): ")) / 100) / 12
    months = float(input("Enter number of months to repay: "))

    repayment = (rate * house_value) / (1 - math.pow((1 + rate), -months))
    print(f"Monthly repayment: R{repayment:.2f}")
