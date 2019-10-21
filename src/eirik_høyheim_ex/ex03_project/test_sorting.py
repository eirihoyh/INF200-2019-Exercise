# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"


def bubble_sort(data):
    """Takes in a tuplet and sorts the numbers inside"""
    new_data = list(data)
    swap = True
    while swap:
        swap = False
        for i in range(len(new_data) - 1):
            if new_data[i] > new_data[i + 1]:
                temp = new_data[i]
                new_data[i] = new_data[i + 1]
                new_data[i + 1] = temp
                swap = True
    return new_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


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
    assert data is not sorted_data


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
    data = [2, 1, 4]
    sorted_data = bubble_sort(data)
    assert sorted_data == sorted(data)


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1, 4, 5, 6]
    data.reverse()
    sorted_data = bubble_sort(data)
    assert sorted_data == [1, 2, 3, 4, 5, 6]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == [1, 1, 1, 1]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data1 = [34, 10021, 2, 100]
    data2 = ["911123", "111", "64", "1", "3452", "732"]
    data3 = [1, 2, 6, 3, 8, 5, 2, 1, 6, 90, 4, 2, 1]
    sorted_data1 = bubble_sort(data1)
    sorted_data2 = bubble_sort(data2)
    sorted_data3 = bubble_sort(data3)
    assert sorted_data1 == sorted(data1)
    assert sorted_data2 == sorted(data2)
    assert sorted_data3 == sorted(data3)
