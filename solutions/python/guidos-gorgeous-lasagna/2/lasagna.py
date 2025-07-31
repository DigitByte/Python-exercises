"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module contains functions related to preparing and timing
a lasagna recipe.
"""

EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate the preparation time based on the number of layers.

    :param layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes).
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate total time spent preparing and baking the lasagna.

    :param layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time (in minutes) spent preparing and baking.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
