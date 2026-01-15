def withdraw(balance, amount):
    if balance > amount:
        raise ValueError
    if amount > balance:
        return balance
    return balance - amount
