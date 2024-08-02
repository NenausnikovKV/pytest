"""
Рабочие функции
"""


def sum2(x, y):
    """ Складываем 2 числа """
    return x + y


def plus2(nums):
    """ Прибавляем 2 к каждому элементу коллекции """
    result = []
    for num in nums:
        result.append(num + 2)
    return result


def multiply2(nums):
    """ Умножаем на 2 каждый элемент коллекции """
    result = []
    for num in nums:
        result.append(num * 2)
    return result


def exponent2(nums):
    """ Возводим в степень 2 каждый элемент коллекции"""
    result = []
    for num in nums:
        result.append(num ** 2)
    return result


def positive_or_negative(x):
    """ Конвертируем число в строку """
    if x > 0:
        return 'positive'
    if x < 0:
        return 'negative'
    return 'zero'
