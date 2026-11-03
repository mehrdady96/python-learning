"""
A simple module for calculating currency exchange values
"""


def exchange_money(budget, exchange_rate):
    """
    Calculate how much foreign currency can be received.

    budget (float): The amount of money available to exchange.
    exchange_rate (float): The amount of domestic currency equal to one
                           unit of foreign currency.
    """
    exchanged_amount = budget / exchange_rate
    # exchanged_amount (float): The amount of foreign currency received
    return exchanged_amount


def get_change(budget, exchanging_value):
    """
    Calculate how much money remains after an exchange.

    budget (float): The amount of money before the exchange.
    exchanging_value (float): The amount of money used for the exchange.
    """
    remaining_amount = budget - exchanging_value
    # remaining_amount (float): The money left after the exchange
    return remaining_amount


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of a number of bills.

    denomination (int): The value of one bill.
    number_of_bills (int): The number of bills.
    """
    total_value = denomination * number_of_bills
    # total_value (int): The combined value of all bills
    return total_value


def get_number_of_bills(amount, denomination):
    """
    Calculate how many whole bills fit into an amount.

    amount (float): The amount of money available.
    denomination (int): The value of one bill.
    """
    number_of_bills = int(amount // denomination)
    # number_of_bills (int): The number of whole bills
    return number_of_bills


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the amount left after taking whole bills.

    amount (float): The amount of money available.
    denomination (int): The value of one bill.
    """
    leftover = amount % denomination
    # leftover (float): The amount that cannot be paid as a whole bill
    return leftover


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the total value of whole bills received after an exchange.

    budget (float): The amount of money available to exchange.
    exchange_rate (float): The original exchange rate.
    spread (int): The exchange fee as a percentage.
    denomination (int): The value of one bill in the new currency.
    """
    spread = spread / 100
    # spread (float): The exchange fee converted to a decimal

    exchange_rate = exchange_rate * (1 + spread)
    # exchange_rate (float): The exchange rate including the fee

    exchanged_amount = budget / exchange_rate
    # exchanged_amount (float): The amount of new currency received

    number_of_bills = int(exchanged_amount // denomination)
    # number_of_bills (int): The number of whole bills received

    total_value = number_of_bills * denomination
    # total_value (int): The total value of the whole bills
    return total_value