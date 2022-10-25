"""CSC111 Winter 2022 Prep 2: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the implementation of linked lists we studied in lecture
last week, including the append method and updated initializer from the prep reading.

There are two additional methods at the bottom of the class that we have started.
Your first task is to implement EACH method based on the method header and description.

Your second task is to write a set of tests for each of the methods, as described at the bottom
of this file. This is good review of how to write unit tests in Python from CSC110, which you'll
need to do throughout this course.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You do not need to add additional doctests. However, you should test your work carefully
before submitting it!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr and David Liu.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional

import pytest  # You'll need to use pytest.raises in your tests (see below)


@dataclass
class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for item in items:
            self.append(item)

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def append(self, item: Any) -> None:
        """Append item to the end of this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.append(4)
        >>> lst.to_list()
        [1, 2, 3, 4]
        """
        new_node = _Node(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    ############################################################################
    # Prep exercises start here
    ############################################################################
    def remove_first(self) -> Any:
        """Remove and return the first element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_first()
        1
        >>> lst.to_list()
        [2, 3]
        >>> lst.remove_first()
        2
        >>> lst.remove_first()
        3
        """
        if self._first is None:
            raise IndexError
        else:
            first_node_value = self._first.item
            next_node = self._first.next
            self._first = next_node
            return first_node_value

    def remove_last(self) -> Any:
        """Remove and return the last element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_last()
        3
        >>> lst.to_list()
        [1, 2]
        >>> lst.remove_last()
        2
        >>> lst.remove_last()
        1

        IMPLEMENTATION HINTS:
            1. You'll need to modify the linked list traversal pattern to reach
               the *second-last node*.
            2. It's okay to have separate cases (using if statements) for size-0
               and size-1 linked lists.
        """
        if self._first is None:
            raise IndexError
        elif self._first.next is None:
            first = self._first.item
            self._first = None
            return first
        else:
            curr = self._first
            while curr.next.next is not None:
                curr = curr.next
            if curr.next.next is None:
                remove = curr.next.item
                curr.next = None
                return remove


################################################################################
# Test cases
################################################################################
# Write unit tests for each of the two LinkedList methods you implemented above.
# Your tests should cover various cases for possible linked list lengths, and
# should check both for mutation and the correct return value.
# You can use the LinkedList.to_list method to check the values in the linked list.
# Each unit test should have a docstring containing a brief description of the test.
#
# To review how to write unit tests using pytest (including testing for errors being raised),
# please consult
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html.
#
# WARNING: your test function names MUST start with "test_", otherwise they won't
# be detected as unit tests by pytest, and therefore won't be run.

def test_remove_first_for_length_1() -> None:
    """Test the mutation, return value of remove_first
    on a length one linked list.
    """
    linky = LinkedList([1])
    expected_remove_value = 1
    expected_new_linky = LinkedList([]).to_list()
    actual_remove_value = linky.remove_first()
    actual_new_linky = linky.to_list()
    assert expected_remove_value == actual_remove_value and expected_new_linky == actual_new_linky


def test_remove_first_for_length_0() -> None:
    """Test raising IndexError exception of remove_first
    on a empty linked list.
    """
    linky = LinkedList([])
    expected_new_linky = LinkedList([]).to_list()
    with pytest.raises(IndexError):
        linky.remove_first()
        actual_new_linky = linky.to_list()
        assert expected_new_linky == actual_new_linky


def test_remove_last_for_length_1() -> None:
    """Test the mutation, return value of remove_last
    on a length one linked list.
    """
    linky = LinkedList([1])
    expected_remove_value = 1
    expected_new_linky = LinkedList([]).to_list()
    actual_remove_value = linky.remove_last()
    actual_new_linky = linky.to_list()
    assert expected_remove_value == actual_remove_value and expected_new_linky == actual_new_linky


def test_remove_last_for_length_2() -> None:
    """Test the mutation, return value of remove_last
    on a length two linked list.
    """
    linky = LinkedList([1, 2])
    expected_remove_value = 2
    expected_new_linky = LinkedList([1]).to_list()
    actual_remove_value = linky.remove_last()
    actual_new_linky = linky.to_list()
    assert expected_remove_value == actual_remove_value and expected_new_linky == actual_new_linky


def test_remove_last_for_length_3() -> None:
    """Test the mutation, return value of remove_last
    on a length three linked list.
    """
    linky = LinkedList([1, 2, 3])
    expected_remove_value = 3
    expected_new_linky = LinkedList([1, 2]).to_list()
    actual_remove_value = linky.remove_last()
    actual_new_linky = linky.to_list()
    assert expected_remove_value == actual_remove_value and expected_new_linky == actual_new_linky


def test_remove_last_for_length_0() -> None:
    """Test raising IndexError exception of remove_last
    on a empty linked list.
    """
    linky = LinkedList([])
    expected_new_linky = LinkedList([]).to_list()

    with pytest.raises(IndexError):
        linky.remove_last()
        actual_new_linky = linky.to_list()
        assert expected_new_linky == actual_new_linky


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()

    pytest.main(['prep2.py', '-v'])
