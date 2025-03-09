import random


def get_lottery_numbers(min_num: int, max_num: int, quantity: int) -> list:
    """
    Function to generate a set of unique lottery numbers
    :param min_num: Minimum possible number in the set (at least 1)
    :param max_num: Maximum possible number in the set (no more than 1000)
    :param quantity: The number of unique numbers to generate
    :return: Sorted list of unique random numbers
    """
    if (not (1 <= min_num <= max_num <= 1000) or
            quantity > (max_num - min_num + 1)
    ):
        return []
    return sorted(random.sample(range(min_num, max_num + 1), quantity))