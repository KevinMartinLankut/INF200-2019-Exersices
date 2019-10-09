# -*- coding: utf-8 -*-
import pytest


__author__ = 'Kevin Martin Lankut'
__email__ = 'kela@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data

    Code gotten from:
    https://github.com/yngvem/INF200-2019-Exercises/blob/master/exersices/ex03.rst
    """
    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError
    else:
        return (sdata[n // 2] if n % 2 == 1
                else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_one_elem_list():
    data = [1, 2, 3, 4]
    result = [median(data)]
    assert len(result) == 1


def test_odd_and_reversed():
    data = [3, 2, 1]
    correct = 2
    assert median(data) == correct


def test_even_and_ordered():
    data = [1, 2, 3, 4]
    correct = 2.5
    assert median(data) == correct


def test_unordered():
    data = [5, 1, 3, 10, 6]
    correct = 5
    assert median(data) == correct


def test_empty_list_error():
    with pytest.raises(ValueError):
        median([])


def test_original_untouched():
    data = [1, 2, 3, 4]
    original = data
    median_res = median(data)
    assert data is original
    assert data is not median_res


def test_tupler():
    data = (1, 2, 3, 4)
    correct = 2.5
    assert median(data) == correct
