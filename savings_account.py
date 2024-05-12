
"""Import the Account class from the Account.py file.""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
 from Accounts import Account

def create_savings_account(balance, interest):
    account = Account(balance, interest)
    interest_earned = account.balance * (account.interest / 100)
    new_balance = account.balance + interest_earned
    account.set_balance(new_balance)
    account.set_interest(interest_earned)
    return account.balance, interest_earned

