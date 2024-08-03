""" Вспоминаю как работает pytest """
# отключаем проверку для использования фикстур
# pylint: disable=redefined-outer-name

import pytest

# pylint: disable-next=import-error
from arithmethic_methods.arithmethic_methods import sum2, plus2, multiply2, exponent2, positive_or_negative

MORE_ZERO_DIGIT = 1


@pytest.fixture(scope='module', autouse=True)
def say_hello():
    """Фикстура, вызываемая при тестах всегда, не требует привязки к тесту"""
    print("Test start")


@pytest.fixture(scope='module')
def get_min_num():
    """ Берем нижнюю границу для списка простых чисел """
    return 1


@pytest.fixture(scope='module')
def get_max_num():
    """ Берем верхнюю границу для списка простых чисел """
    return 50


@pytest.fixture(scope='module')
def get_prime_nums(get_min_num, get_max_num):
    """ Берем простые числа от 1 до 50 """
    prime_nums = []
    for num in range(get_min_num, get_max_num):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            prime_nums.append(num)
    yield prime_nums
    print("\nТестирование завершено")


def test_plus2(get_prime_nums):
    """Проверка прибавления 2 к каждому элементу итерируемого объекта"""
    prime_nums = get_prime_nums
    assert plus2(prime_nums) == [3, 4, 5, 7, 9, 13, 15, 19, 21, 25, 31, 33, 39, 43, 45, 49], "Ошибка прибавления 2"


def test_sum2():
    """ Проверка сложения двух чисел"""
    assert sum2(15, 8) == 23, "Неверное сложение"


def test_multiply2(get_prime_nums):
    """Проверка умножения на 2 каждого элемента итерируемого объекта"""
    prime_nums = get_prime_nums
    correct_answers = [2, 4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94]
    assert multiply2(prime_nums) == correct_answers, "Ошибка умножения на 2"


def test_exponent2(get_prime_nums):
    """Проверка возведения в степень 2 каждого элемента итерируемого объекта"""
    prime_nums = get_prime_nums
    correct_answers = [1, 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, 1681, 1849, 2209]
    assert exponent2(prime_nums) == correct_answers, "Ошибка возведения во 2 степень"


@pytest.mark.skip(reason="test skipping")
def test_skipped():
    """Тест для пропуска теста"""


@pytest.mark.skipif(MORE_ZERO_DIGIT > 0, reason="because condition digit more than 0")
def test_skipped_if():
    """ Пропуск теста по условию """


@pytest.mark.parametrize("x", [165, 1.2, 0.00000001])
def test_negative_or_positive_if_positive(x):
    """Проверка на положительных числах"""
    assert positive_or_negative(x) == "positive"


@pytest.mark.parametrize("x, expected_result",
                         [
                             (165, 'positive'),
                             (1.2, 'positive'),
                             (0.0000001, 'positive'),
                             (-165, 'negative'),
                             (-1.2, 'negative'),
                             (-0.0000001, 'negative'),
                             (0, 'zero')
                         ])
def test_negative_or_positive(x, expected_result):
    """ Проверка на положительных и отрицательных числах """
    assert positive_or_negative(x) == expected_result


@pytest.mark.my_mark
def test_with_personal_mark():
    pass
