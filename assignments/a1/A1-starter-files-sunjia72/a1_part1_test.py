"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

Please write your tests for Part 1 in this module. Make sure to review the assignment
instructions carefully for this part! You may find it helpful to consult this
section of the Course Notes:
https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html

While you must include unit tests, you may also use property-based tests in your test suite.

We will *not* be running PythonTA on this file; however, you should follow good programming
design and style in this file anyway, just like you would for all other work.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
import pytest

from a1_part1 import MoveToFrontLinkedList, SwapLinkedList, CountLinkedList
from a1_part1 import _CountNode


def test_move_to_front_empty_return() -> None:
    """Test return value of
    empty MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_move_to_front_empty_mutation() -> None:
    """Test the mutation of
    empty MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([])
    expected_new_linky = MoveToFrontLinkedList([]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_move_to_front_1_true_return() -> None:
    """Test return value of
    length-1 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_move_to_front_1_true_mutation() -> None:
    """Test the mutation of
    length-1 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1])
    expected_new_linky = MoveToFrontLinkedList([1]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_move_to_front_1_false_return() -> None:
    """Test return value of
    length-1 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(2)
    assert expected_remove_value == actual_remove_value


def test_move_to_front_1_false_mutation() -> None:
    """Test the mutation of
    length-1 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1])
    expected_new_linky = MoveToFrontLinkedList([1]).to_list()
    linky.__contains__(2)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_move_to_front_2_return() -> None:
    """Test return value of
    length-2 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1, 2])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(2)
    assert expected_remove_value == actual_remove_value


def test_move_to_front_2_mutation() -> None:
    """Test the mutation of
    length-2 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1, 2])
    expected_new_linky = MoveToFrontLinkedList([2, 1]).to_list()
    linky.__contains__(2)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_move_to_front_3_return() -> None:
    """Test return value of
    length-3 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1, 2, 3])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_move_to_front_3_mutation() -> None:
    """Test the mutation of
    length-3 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1, 2, 3])
    expected_new_linky = MoveToFrontLinkedList([1, 2, 3]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_move_to_front_4_return() -> None:
    """Test return value of
    length-4 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1, 2, 3, 4])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(6)
    assert expected_remove_value == actual_remove_value


def test_move_to_front_4_mutation() -> None:
    """Test the mutation of
    length-4 MoveToFrontLinkedList.__contains__.
    """
    linky = MoveToFrontLinkedList([1, 2, 3, 4])
    expected_new_linky = MoveToFrontLinkedList([1, 2, 3, 4]).to_list()
    linky.__contains__(6)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_swap_empty_return() -> None:
    """Test return value of
    empty SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_swap_empty_mutation() -> None:
    """Test the mutation of
    empty SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([])
    expected_new_linky = SwapLinkedList([]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_swap_1_true_return() -> None:
    """Test return value of
    length-1 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_swap_1_true_mutation() -> None:
    """Test the mutation of
    length-1 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1])
    expected_new_linky = SwapLinkedList([1]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_swap_1_false_return() -> None:
    """Test return value of
    length-1 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(3)
    assert expected_remove_value == actual_remove_value


def test_swap_1_false_mutation() -> None:
    """Test the mutation of
    length-1 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1])
    expected_new_linky = SwapLinkedList([1]).to_list()
    linky.__contains__(3)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_swap_2_return() -> None:
    """Test return value of
    length-2 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1, 2])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(2)
    assert expected_remove_value == actual_remove_value


def test_swap_2_mutation() -> None:
    """Test the mutation of
    length-2 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1, 2])
    expected_new_linky = SwapLinkedList([2, 1]).to_list()
    linky.__contains__(2)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_swap_3_return() -> None:
    """Test return value of
    length-3 SwapLinkedList.__contains__
    """
    linky = SwapLinkedList([1, 2, 3])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(3)
    assert expected_remove_value == actual_remove_value


def test_swap_3_mutation() -> None:
    """Test the mutation of
    length-3 SwapLinkedList.__contains__
    """
    linky = SwapLinkedList([1, 2, 3])
    expected_new_linky = SwapLinkedList([1, 3, 2]).to_list()
    linky.__contains__(3)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_swap_4_return() -> None:
    """Test return value of
    length-4 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1, 2, 3, 4])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(4)
    assert expected_remove_value == actual_remove_value


def test_swap_4_mutation() -> None:
    """Test the mutation of
    length-4 SwapLinkedList.__contains__.
    """
    linky = SwapLinkedList([1, 2, 3, 4])
    expected_new_linky = SwapLinkedList([1, 2, 4, 3]).to_list()
    linky.__contains__(4)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_empty_return() -> None:
    """Test return value of
    empty CountLinkedList.__contains__.
    """
    linky = CountLinkedList([])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_count_empty_mutation() -> None:
    """Test the mutation of
    empty CountLinkedList.__contains__.
    """
    linky = CountLinkedList([])
    expected_new_linky = CountLinkedList([]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_1_true_return() -> None:
    """Test return value of
    length-1 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(1)
    assert expected_remove_value == actual_remove_value


def test_count_1_true_mutation() -> None:
    """Test the mutation of
    length-1 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1])
    expected_new_linky = CountLinkedList([1]).to_list()
    linky.__contains__(1)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_1_false_return() -> None:
    """Test return value of
    length-1 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1])
    expected_remove_value = False
    actual_remove_value = linky.__contains__(3)
    assert expected_remove_value == actual_remove_value


def test_count_1_false_mutation() -> None:
    """Test the mutation of
    length-1 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1])
    expected_new_linky = CountLinkedList([1]).to_list()
    linky.__contains__(3)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_2_mutation() -> None:
    """Test the mutation of
    length-2 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1, 2])
    expected_new_linky = CountLinkedList([2, 1]).to_list()
    linky.__contains__(2)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_2_return() -> None:
    """Test return value of
    length-2 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1, 2])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(2)
    assert expected_remove_value == actual_remove_value


def test_count_3_mutation() -> None:
    """Test the mutation of
    length-3 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1, 2, 3])
    expected_new_linky = CountLinkedList([2, 1, 3]).to_list()
    linky.__contains__(2)
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_3_return() -> None:
    """Test return value of
    length-3 CountLinkedList.__contains__.
    """
    linky = CountLinkedList([1, 2, 3])
    expected_remove_value = True
    actual_remove_value = linky.__contains__(2)
    assert expected_remove_value == actual_remove_value


def test_count_6_mutation() -> None:
    """Test the mutation of
    length-6 CountLinkedList.__contains__.
    """
    a1 = _CountNode(item=10, access_count=123)
    a2 = _CountNode(item=20, access_count=122)
    a3 = _CountNode(item=30, access_count=122)
    a4 = _CountNode(item=40, access_count=122)
    a5 = _CountNode(item=50, access_count=44)
    a6 = _CountNode(item=60, access_count=0)
    a5.next = a6
    a4.next = a5
    a3.next = a4
    a2.next = a3
    a1.next = a2
    linky = CountLinkedList([])
    linky._first = a1
    linky.__contains__(40)
    expected_new_linky = CountLinkedList([10, 40, 20, 30, 50, 60]).to_list()
    actual_new_linky = linky.to_list()
    assert expected_new_linky == actual_new_linky


def test_count_6_return() -> None:
    """Test return value of
    length-6 CountLinkedList.__contains__.
    """
    a1 = _CountNode(item=10, access_count=123)
    a2 = _CountNode(item=20, access_count=122)
    a3 = _CountNode(item=30, access_count=122)
    a4 = _CountNode(item=40, access_count=122)
    a5 = _CountNode(item=50, access_count=44)
    a6 = _CountNode(item=60, access_count=0)
    a5.next = a6
    a4.next = a5
    a3.next = a4
    a2.next = a3
    a1.next = a2
    linky = CountLinkedList([])
    linky._first = a1
    expected_remove_value = True
    actual_remove_value = linky.__contains__(40)
    assert expected_remove_value == actual_remove_value


if __name__ == '__main__':
    pytest.main(['a1_part1_test.py', '-v'])
