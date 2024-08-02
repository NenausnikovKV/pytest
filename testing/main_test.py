""" Вспоминаю как работает pytest """
# отключаем проверку для использования фикстур
# pylint: disable=redefined-outer-name

import pytest

from arithmethic_methods import sum2, plus2, multiply2, exponent2


@pytest.fixture()
def get_prime_nums():
    """ Берем простые числа от 1 до 50 """
    print('\nРабота фикстуры')
    prime_nums = []
    for num in range(1, 50):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    yield prime_nums
    print("\nТестирование завершено")


def test_sum2():
    """ Проверка сложения двух чисел"""
    assert sum2(15, 8) == 23


def test_plus2(get_prime_nums):
    """Проверка прибавления 2 к каждому элементу итерируемого объекта"""
    prime_nums = get_prime_nums
    assert plus2(prime_nums) == [3, 4, 5, 7, 9, 13, 15, 19, 21, 25, 31, 33, 39, 43, 45, 49]


def test_multiply2(get_prime_nums):
    """Проверка умножения на 2 каждого элемента итерируемого объекта"""
    prime_nums = get_prime_nums
    assert multiply2(prime_nums) == [2, 4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94]


def test_exponent2(get_prime_nums):
    """Проверка возведения в степень 2 каждого элемента итерируемого объекта"""
    prime_nums = get_prime_nums
    assert exponent2(prime_nums) == [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209]
