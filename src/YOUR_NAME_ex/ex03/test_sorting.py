# -*- coding: utf-8 -*-

__author__ = 'Kevin Martin Lankut'
__email__ = 'kela@nmbu.no'


def bubble_sort(data):
    # Gotten from my TA Daniel Pricne
    data = list(data)
    sorting_lengh = len(data) - 1
    for i in range(sorting_lengh):
        for j in range(sorting_lengh - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def test_tupler():
    """Test that the sorting function works for tuplers, should return lists"""
    tupler_data = (1, 2, 3)
    data = [1, 2, 3]
    assert bubble_sort(data) == bubble_sort(tupler_data)


def test_empty():
    """Test that the sorting function works for empty list"""

    data = []
    assert bubble_sort(data) == []


def test_single():
    """Test that the sorting function works for single-element list"""

    data = [5]
    assert bubble_sort(data) == [5]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert bubble_sort(sorted_data)


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    reverse_data = [1, 2, 3]
    assert bubble_sort(data) == bubble_sort(reverse_data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1, 1]
    assert bubble_sort(data)


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data1 = [4, 2, 3, 1]
    data2 = ['b', 'c', 'a']
    assert bubble_sort(data1) == [1, 2, 3, 4]
    assert bubble_sort(data2) == ['a', 'b', 'c']
