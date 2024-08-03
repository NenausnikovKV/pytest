"""
Тесты исключений
"""
import warnings

import pytest


def test_zero_division():
    """Проверка поднятия исключения деления на ноль"""
    with pytest.raises(ZeroDivisionError):
        print(1 / 0)


def test_exception_value_match():
    """Проверка содержимого исключения"""
    with pytest.raises(ZeroDivisionError) as exc_info:
        print(1/0)
    assert "division by zero" in str(exc_info.value)


def test_match():
    """Проверка описания исключения в блоке with as"""
    with pytest.raises(ValueError, match="123"):
        raise ValueError("Exception 123 raised")


@pytest.mark.xfail(raises=IndexError)
def test_index_error():
    """Проверка ошибки индекса"""
    a = [1, 2]
    print(a[1])


@pytest.mark.xfail(reason="Expected failure")
def test_expected_failed():
    """ Ожидаемый провал теста """
    assert False


def test_warning():
    """Проверка предупреждений"""
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)
