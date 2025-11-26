import pytest
from src.sorts import (bubble_sort, quick_sort,
                       counting_sort, radix_sort, bucket_sort)
from src.heap_sort import (heap_sort)
from src.stack import Stack
from src.fibonacci_and_factorial import fibo, fibo_recursive, factorial, factorial_recursive


# Ошибки сортировок
def test_bubble_sort_empty_list():
    try:
        bubble_sort([])
    except ValueError:
        assert True
    else:
        assert False


def test_bubble_sort_wrong_type():
    try:
        bubble_sort([2.5, 5.6])  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_quick_sort_wrong_type():
    try:
        quick_sort([2.6, 6.5])  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_counting_sort_empty_list():
    try:
        counting_sort([])
    except ValueError:
        assert True
    else:
        assert False


def test_counting_sort_wrong_type():
    try:
        counting_sort([2.6, 6.5])  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_radix_sort_empty_list():
    try:
        radix_sort([])
    except ValueError:
        assert True
    else:
        assert False


def test_radix_sort_wrong_type():
    try:
        radix_sort([2.6, 6.5])  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_bucket_sort_empty_list():
    try:
        radix_sort([])
    except ValueError:
        assert True
    else:
        assert False


def test_bucket_sort_wrong_type():
    try:
        bucket_sort([2, 6])  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_heap_sort_empty_list():
    try:
        heap_sort([])
    except ValueError:
        assert True
    else:
        assert False


def test_heap_sort_wrong_type():
    try:
        heap_sort([2.6, 6.5])  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


# Ошибки стека
def test_pop_from_empty_stack():
    test = Stack()

    try:
        test.pop()
    except IndexError:
        assert True
    else:
        assert False


def test_peek_from_empty_stack():
    test = Stack()

    try:
        test.peek()
    except IndexError:
        assert True
    else:
        assert False


# Ошибки факториала и фибонначи
def test_factorial_wrong_type():
    try:
        factorial(2.5)  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_factorial_recursive_wrong_type():
    try:
        factorial_recursive(5.6)  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_fibo_wrong_type():
    try:
        fibo(2.5)  # type: ignore
    except ValueError:
        assert True
    else:
        assert False


def test_fibo_recursive_wrong_type():
    try:
        fibo_recursive(5.6)  # type: ignore
    except ValueError:
        assert True
    else:
        assert False
