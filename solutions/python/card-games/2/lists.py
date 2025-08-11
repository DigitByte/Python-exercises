"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate and return the average card value from the list."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Return if approx averages (first+last)/2 or middle card == true average."""
    true_avg = card_average(hand)
    approx_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    return true_avg in (approx_avg, middle_card)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Return if the average of even-indexed card values == average of odd-indexed card values."""
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    return card_average(even_cards) == card_average(odd_cards)


def maybe_double_last(hand: list[int]) -> list[int]:
    """Multiply a Jack card (value 11) in the last index position by 2."""
    if hand and hand[-1] == 11:
        hand[-1] *= 2
    return hand
