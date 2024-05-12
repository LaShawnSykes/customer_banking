from Accounts import Account

def create_savings_account(balance, interest):
    account = Account(balance, interest)
    interest_earned = account.balance * (account.interest / 100)
    new_balance = account.balance + interest_earned
    account.set_balance(new_balance)
    account.set_interest(interest_earned)
    return account.balance, interest_earned
