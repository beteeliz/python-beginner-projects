def main():
    print("This is a monthly payment loan calculator")
    print("\n")

    principal = float(input("Write the loan amount: "))
    apr = float(input("Write the annual interest rate: "))
    years = int(input("Write the amount of years: "))

    monthly_interest_rate = apr / 1200
    number_of_months = years * 12
    monthly_pament = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-number_of_months))

    print("The monthly pament for this loan is: %.2f" % monthly_pament)

main()