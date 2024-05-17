import math

user_input = input("""
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()

while True:
    if user_input == 'investment':
        print("Investment option selected.")
        money_deposited = int(input("How much money will you be depositing?: "))
        interest_rate = int(input("What is the interest rate? Please enter a whole number between 1 and 100: "))
        years_invested = int(input("How many years will you be investing for?: "))
        interest = input("Do you want simple or compound interest? Please enter either 'simple' or 'compound': ").lower()

        if interest == "simple":
            simple_interest = money_deposited * (1 + (interest_rate / 100) * years_invested)
            print(f"The total amount of money you will have after {years_invested} years is {int(simple_interest)} pounds")
        elif interest == "compound":
            compound_interest = money_deposited * math.pow((1 + (interest_rate / 100)), years_invested)
            print(f"The total amount of money you will have after {years_invested} years is {int(compound_interest)} pounds")
        else:
            print("Invalid input. Please enter either 'simple' or 'compound'.")
        break

    elif user_input == 'bond':
        print("Bond option selected.")
        present_value = float(input("What is the present value (market value) of the house?: "))
        interest_rate = float(input("What is the annual interest rate (as a percentage)?: "))
        number_of_months = int(input("Over how many months will the bond be repaid?: "))

        # Bond repayment calculation
        monthly_interest_rate = interest_rate / 100 / 12
        bond_repayment = present_value * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_months)) / (math.pow(1 + monthly_interest_rate, number_of_months) - 1)

        print(f"The monthly repayment on the bond will be: {round(bond_repayment, 2)}")
        break

    else:
        print("Invalid input. Please enter either 'investment' or 'bond'.")
        break

#There seems to be a syntax Error: invalid syntax when I run the program on VS code but it works in replit?
# refreshed the VS Code and now it works - any idea what the issue could have been?