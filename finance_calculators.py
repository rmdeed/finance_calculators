import math

# Print the choices for the calculator and request an input from the user
calculation = input("""investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Choose either 'investment' or 'bond' from the menu above to proceed: """).lower()

# Calculations for if the user inputs investment and outputs
if calculation == "investment":
    P = round(float(input("Enter the amount you want to deposit in pounds (do not add the £ symbol): ")), 2)
    r = round(float(input("Enter the yearly interest rate (do not add the % symbol): ")), 2) / 100
    t = round(float(input("Enter the number of years you wish to invest for: ")), 2)
    interest = input("Enter if you want 'simple' or 'compound' interest: ").lower()
    if interest == "simple":
        A = P * (1 + r * t)
        print(f"Your total amount will be £{round(A, 2)}")
    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print(f"Your total amount will be £{round(A, 2)}")
    else:
        print("Something went wrong. Please try again.")
# Calculations for if the user inputs bond and outputs
elif calculation == "bond":
    P = round(float(input("The present value of the house: ")), 2)
    i = (round(float(input("Enter the yearly interest rate (do not add the % symbol): ")), 2) / 100) / 12
    n = round(float(input("Enter the number of months you wish to repay the bond: ")), 2)
    x = (i * P) / (1 - math.pow((1 + i), -n))
    print(f"You will have to repay £{round(x, 2)} each month")
# Error message if user inputs anything else
else:
    print("Something went wrong. Please try again.")
