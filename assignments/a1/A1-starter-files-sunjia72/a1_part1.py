"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

This Python module contains three linked list subclasses corresponding to the three
moving heuristics described on the assignment handout.

You need to complete their implementations by overriding the __contains__ method
(and only for CountLinkedList, additional methods as required).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from a1_linked_list import LinkedList, _Node


################################################################################
# Heuristic 1 (move to front)
################################################################################
class MoveToFrontLinkedList(LinkedList):
    """A linked list implementation that uses a "move to front" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
    """

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, move it to the front of this list.

        >>> linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [40, 10, 20, 30, 50, 60]
        """
        curr = self._first
        if curr is None:
            return False
        if curr.item == item:
            return True
        while curr.next is not None:
            if curr.next.item == item:
                antecent = curr.next.next
                first = self._first
                self._first = curr.next
                self._first.next = first
                curr.next = antecent
                return True
            curr = curr.next
        return False


################################################################################
# Heuristic 2 (swap)
################################################################################


class SwapLinkedList(LinkedList):
    """A linked list implementation that uses a "swap" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
    """

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, swap it with the item before it, if any.
        You may do this by reassigning _Node item or next attributes (or both).

        >>> linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [10, 20, 40, 30, 50, 60]
        >>> linky = SwapLinkedList([10, 20, 30])
        >>> linky.__contains__(30)
        True
        >>> linky.to_list()
        [10, 30, 20]
        """

        curr = self._first
        if curr is None:
            return False
        prev1, prev, curr = None, None, self._first
        while not (curr is None or curr.item == item):
            prev1, prev, curr = prev, curr, curr.next
        if curr is None:
            return False
        else:
            if prev is None and prev1 is None:
                return True
            elif prev1 is None:
                prev.next = curr.next
                curr.next = prev
                self._first = curr
                return True
            else:
                prev.next = curr.next
                curr.next = prev
                prev1.next = curr
                return True


################################################################################
# Heuristic 3 (count)
################################################################################
# NOTE: this heuristic requires a new kind of _Node that has an additional "count" attribute.
@dataclass
class _CountNode(_Node):
    """A node in a CountLinkedList.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
      - access_count: The number of times this node has been accessed (used by the count heuristic)
    """
    next: Optional[_CountNode] = None
    access_count: int = 0


class CountLinkedList(LinkedList):
    """A linked list implementation that uses a "swap" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
        - nodes are sorted in non-increasing order by access_count

    NOTE: In order to make use of the _CountNode class above, you'll need to override every
    LinkedList method in a1_linked_list.py that creates new _Node objects to create _CountNode
    objects instead. Your code for the overridden methods should be otherwise identical.
    """
    _first: Optional[_CountNode]

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

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList([1, 2, 3])
        >>> len(lst)
        3
        """
        curr = self._first
        len_so_far = 0
        while curr is not None:
            len_so_far += 1
            curr = curr.next

        return len_so_far

    def __getitem__(self, i: int) -> Any:
        """Return the item stored at index i in this linked list.

        Raise an IndexError if index i is out of bounds.

        Preconditions:
            - i >= 0
        """
        curr = self._first
        curr_index = 0

        while curr is not None:
            if curr_index == i:
                return curr.item

            curr = curr.next
            curr_index = curr_index + 1

        # If we've reached the end of the list and no item has been returned,
        # the given index is out of bounds.
        raise IndexError

    def pop(self, i: int) -> Any:
        """Remove and return the item at index i.

        Raise IndexError if i >= len(self).

        Preconditions:
            - i >= 0

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.to_list()
        [1, 10, 200]
        """
        if i == 0:
            if self._first is None:
                raise IndexError
            else:
                item = self._first.item
                self._first = self._first.next
                return item
        else:
            curr = self._first
            curr_index = 0

            while not (curr is None or curr_index == i - 1):
                curr = curr.next
                curr_index = curr_index + 1

            if curr is None:
                raise IndexError
            else:
                if curr.next is None:
                    raise IndexError
                else:
                    item = curr.next.item
                    curr.next = curr.next.next
                    return item

    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list.
        """
        new_node = _CountNode(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, increase its count and reorder the nodes in
        non-increasing count order---see assignment handout for details.

        >>> linky = CountLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [40, 10, 20, 30, 50, 60]
        """
        curr = self._first
        if curr is None:
            return False
        prev, curr = None, self._first
        while not (curr is None or curr.item == item):
            prev, curr = curr, curr.next
        if curr is None:
            return False
        else:
            curr.access_count += 1
            if prev is None:  # curr is the first node
                self._first = curr.next
            else:
                prev.next = curr.next  # temporarily delete curr.
            prev1, curr1 = None, self._first
            while not (curr1 is None or curr1.access_count < curr.access_count):
                prev1, curr1 = curr1, curr1.next
            if prev is None and prev1 is None:
                self._first = curr
            elif prev1 is None:
                curr.next = curr1
                self._first = curr
            elif curr1 is None:  # curr should be assigned at the end
                curr.next = None
                prev1.next = curr
            else:  # curr should be between prev and curr.
                curr.next = curr1
                prev1.next = curr
            return True


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136'],
        'extra-imports': ['a1_linked_list'],
        'max-nested-blocks': 4
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
