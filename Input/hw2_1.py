"""

Interest calculator

The program takes 2 inputs from user, principal and interest rate
and print the accrued interest earned every 5 years for the first
50 years.
"""
def main():
    principal = get_input("Please enter principal amount: $", 0, 1000000,
              "Invalid amount. Principal must be between $0 and $1,000,000.00")
    interest_rate = get_input("Please enter interest rate: %", 0, 100,
              "Invalid rate. Interest rate must be between 0 and 100")

    for year in range(5, 51, 5):
        accrued_amount = calc_accrued_amount(principal, interest_rate, year)
        formatted_accrued_amount = f'${accrued_amount:,.2f}'
        print(f'Accrued amount after {year:>2} years: '
              f'{formatted_accrued_amount:>15}')

def get_input(request, lower_bound, upper_bound, error_message):
    """

    Get input from user
    :param request: (String) Request for the user
    :param lower_bound: (number) lower bound of input
    :param upper_bound: (number) upper bound of input
    :param error_message: (String) error for incorrect input
    :return: (number) user input
    """
    validInput = False
    while not validInput:
        value = float(input(request))  # promt user
        if value < lower_bound or value > upper_bound:
            print(error_message)
        else:
            validInput = True
    return value

def calc_accrued_amount(principal, interest_rate, year):
    """

    calculate the accrued interest
    :param principal: (number) principal from 0 to 1,000,000
    :param interest_rate: (number) interest rate from 0 to 100
    :param year: (number) years of interest
    :return: (number) accrued interest earned
    """
    return principal*((interest_rate/100+1)**year)


if __name__ == "__main__":
    main()
