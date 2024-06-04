# ----------------------------------------------------------------------
# Name:        Interest Calculator
# Purpose:     Calculate interest rates
#
# Date:       Spring 2019
# ----------------------------------------------------------------------
"""
Print the interest rates given a principal amount and interest rate.

Prompt the user for a principal amount and interaest rate.
Call respective functions to handle input and output.
"""
def main():
    condition = False # condition to validate principal amount

    # check if principal_amount is valid through check_amount
    while not condition:
        amount = float(input('Please enter principal amount: $'))
        condition = check_amount(amount)

    condition = False # set to False to validate interest_rate

    # check if interest is valid through check_interest
    while not condition:
        interest_rate = float(input('Please enter interest rate: %'))
        condition = check_interest(interest_rate)

    calculate_accrued(amount, interest_rate)


"""
Calculate the accrued amount given principal amount and interest rate

:param principal_amount: (number) the amount to apply the interest to
:param interest_rate: (number) the rate to apply to the amount
"""
def calculate_accrued(principal_amount, interest_rate):
    interest = (1+(interest_rate/100))

    for year in range(5, 55, 5):
        yearly_interest = pow(interest, year)
        amount = principal_amount * yearly_interest
        formatted = f'${amount:,.2f}'
        print(f'Accrued amount after {year:2} years: {formatted:>14}')


"""
Check if principal amount entered is between 0 and 1,000,000

:param principal_amount: (number) must be between 0 and 1,000,000
:return: (boolean) True or False
"""
def check_amount(principal_amount):
    if principal_amount > 1000000 or principal_amount < 0:
        print('Invalid amount. Principal must be between $0 and '
              '$1,000,000,00')
        return False
    return True


"""
Check if interest rate is between 0 and 100.

:param interest_rate: (number) must be between 0 and 100
:return: (boolean) True or False
"""
def check_interest(interest_rate):
    if interest_rate > 100 or interest_rate < 0:
        print('Invalid rate. Interest rate must be between 0 and 100')
        return False
    return True


if __name__ == "__main__":
    main()
