"""
Functions for calculating steps in exchanging currency.
"""

# This function returns how much foreign currency you will get after exchange
def exchange_money(budget, exchange_rate):
    # Divide your money by the exchange rate to get the foreign currency amount
    return budget / exchange_rate


# This function tells you how much of your original money is left after exchanging some
def get_change(budget, exchanging_value):
    # Subtract the exchanged value from your total budget to get the leftover
    return budget - exchanging_value


# This function tells you the total value of all your bills
def get_value_of_bills(denomination, number_of_bills):
    # Multiply the value of one bill by how many bills you have
    return denomination * number_of_bills


# This function calculates how many full bills you can get with a given amount
def get_number_of_bills(amount, denomination):
    # Use integer division (//) to count how many full bills you can get
    return int(amount // denomination)


# This function returns the leftover money that is not enough for a full bill
def get_leftover_of_bills(amount, denomination):
    # Use the modulus operator (%) to find the remaining money after making full bills
    return amount % denomination


# This function calculates how much money you can exchange into full bills
# considering the exchange rate and fee (spread)
def exchangeable_value(budget, exchange_rate, spread, denomination):
    # First, calculate the actual exchange rate including the fee (spread)
    # Spread is a percentage fee added to the rate
    rate_with_spread = exchange_rate * (1 + spread / 100)

    # Convert the budget using the increased exchange rate
    exchanged_amount = budget / rate_with_spread

    # Now determine how many full bills you can get with the exchanged amount
    number_of_bills = int(exchanged_amount // denomination)

    # Return the total value of the bills (denomination × number of bills)
    return denomination * number_of_bills
