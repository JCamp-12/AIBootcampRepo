""" Calculating the cost of a new car"""

def calculate_future_value(current_loan_value, months_remaining, annual_interest_rate):
    """
    Create a function called calculate_future_value
    Args:
        current_loan_value (float): The current loan value
        the annual_interest_rate (float): The APR
        the months_remaining (int): The number of months remaining on the loan

    Returns:
        Prints the future value of the loan as a float.
    """
    future_loan_value = (annual_interest_rate / 12) * current_loan_value * months_remaining
    # Print the future value of the car to 2 decimal places and thousandths.
    print('future loan value = ', future_loan_value)


if __name__ == "__main__":
    # The new_car_loan dictionary.
    new_car_loan = {
        "current_loan_value": 25000,
        "months_remaining": 6,
        "annual_interest_rate": 0.085
        }

    # Set the function call equal to a variable called cost_of_new_car.
    # Pass the relevant information from the dictionary as arguments to the function.
    calculate_future_value(**new_car_loan)
