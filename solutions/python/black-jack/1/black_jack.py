"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.

    1.  'J', 'Q', or 'K' = 10
    2.  'A' = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand."""
    value1 = value_of_card(card_one)
    value2 = value_of_card(card_two)

    if value1 > value2:
        return card_one
    elif value2 > value1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    If there's already an ace in hand, the incoming ace must be valued as 1.
    Otherwise, the ace can be 11 only if the two-card total plus 11 doesn't bust.
    """
    # If an ace is already in hand, the new ace must be worth 1
    if card_one == 'A' or card_two == 'A':
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)
    return 11 if total + 11 <= 21 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'."""
    cards = [card_one, card_two]
    return ('A' in cards) and (
        '10' in cards or any(c in ['J', 'Q', 'K'] for c in cards if c != 'A')
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
