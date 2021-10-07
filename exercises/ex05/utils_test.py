"""Unit tests for list utility functions."""

__author__ = "730449914"

from exercises.ex05.utils import only_evens

from exercises.ex05.utils import sub

from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """Test if an empty list results in an empty the list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_only_evens_not_even() -> None:
    """See if not even numbers results in an empty list."""
    a: list[int] = [5, 7, 3]
    assert only_evens(a) == []


def test_only_evens_some_even() -> None:
    """See if even numbers enters the new list."""
    a: list[int] = [2, 5, 12, 9]
    assert only_evens(a) == [2, 12]


def test_sub_negative_end() -> None:
    """Does negative end result in empty list."""
    b: list[int] = [1, 7, 9]
    c: int = 0
    d: int = -2
    assert sub(b, c, d) == []


def test_sub_not_inclusive() -> None:
    """See if end is not inclusive."""
    b: list[int] = [1, 2, 3]
    c: int = 1
    d: int = 2
    assert sub(b, c, d) == [2]


def test_sub_many_items() -> None:
    """Test many items."""
    b: list[int] = [1, 5, 8, 2, 43, 0]
    c: int = 0
    d: int = 5
    assert sub(b, c, d) == [1, 5, 8, 2, 43]


def test_concat_empty_lists() -> None:
    """Two empty lists results in one empty list."""
    e: list[int] = []
    f: list[int] = []
    assert concat(e, f) == []


def test_concat_many_items() -> None:
    """Test many items."""
    e: list[int] = [1, 5, 8, 2, 43, 0]
    f: list[int] = [1, 7, 8, 2, 3, 2]
    assert concat(e, f) == [1, 5, 8, 2, 43, 0, 1, 7, 8, 2, 3, 2]


def test_concat_big_numbers() -> None:
    """Test big numbers."""
    e: list[int] = [42, 122, 7896]
    f: list[int] = [70000]
    assert concat(e, f) == [42, 122, 7896, 70000]