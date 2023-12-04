"""
Домашнее задание №1
Функции и структуры данных
"""

from typing import List


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def find_prime(n: int):
    """
    Функция проверки - простое число или нет
    :param n:
    :return:
    """
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def filter_numbers(numbers: List, filter_types: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = None

    if filter_types == ODD:
        result = [n for n in numbers if n & 1]
    if filter_types == EVEN:
        result = [n for n in numbers if not n & 1]
    if filter_types == PRIME:
        result = list(filter(find_prime, numbers))
    return result
