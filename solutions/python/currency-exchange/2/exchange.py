# Functions for calculating steps in exchanging currency.

# Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/


def exchange_money(budget, exchange_rate):
    """
    Calculate how much foreign currency you can get.

    :param budget: float - total amount of money you have to exchange.
    :param exchange_rate: float - cost of one unit of the foreign currency.
    :return: float - amount of foreign currency you will receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate how much money will be left after exchange.

    :param budget: float - your original amount of money.
    :param exchanging_value: float - how much you're exchanging.
    :return: float - leftover amount after the exchange.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of your bills.

    :param denomination: int - value of each bill.
    :param number_of_bills: int - how many bills you have.
    :return: int - total value of all the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Determine how many bills you can get with the given amount.

    :param amount: float - total amount of money available.
    :param denomination: int - value of each bill.
    :return: int - number of bills you can get.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Calculate how much money is left after taking out full bills.

    :param amount: float - total amount of money.
    :param denomination: int - value of each bill.
    :return: float - money that can’t be used for full bills.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value you can receive in whole bills after exchange.

    :param budget: float - how much money you are exchanging.
    :param exchange_rate: float - the actual exchange rate (without spread).
    :param spread: int - percentage fee taken by the exchange service.
    :param denomination: int - value of each bill in foreign currency.
    :return: int - total value in foreign currency you can receive (in whole bills).
    """
    # Convert spread (percentage) to decimal and add to exchange rate
    adjusted_rate = exchange_rate * (1 + spread / 100)
    exchanged = budget / adjusted_rate
    return int(exchanged // denomination) * denomination
