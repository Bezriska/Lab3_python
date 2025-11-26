import pytest
from src.sorts import (bubble_sort, quick_sort,
                       counting_sort, radix_sort, bucket_sort)
from src.heap_sort import (heap_sort)
from src.fibonacci_and_factorial import factorial, factorial_recursive, fibo, fibo_recursive
from src.generators import (rand_int_array, rand_float_array)
from src.stack import Stack


# Тесты сортировок
def test_bubble_sort():
    nums = rand_int_array(10, -50, 50)

    func_res = bubble_sort(nums)
    test_res = sorted(nums)

    assert test_res == func_res


def test_quick_sort():
    nums = rand_int_array(10, -50, 50)

    func_res = quick_sort(nums)
    test_res = sorted(nums)

    assert test_res == func_res


def test_counting_sort():
    nums = rand_int_array(10, -50, 50)

    func_res = counting_sort(nums)
    test_res = sorted(nums)

    assert test_res == func_res


def test_radix_sort():
    nums = rand_int_array(10, -50, 50)

    func_res = radix_sort(nums)
    test_res = sorted(nums)

    assert test_res == func_res


def test_bucket_sort():
    nums = rand_float_array(10)

    func_res = bucket_sort(nums)
    test_res = sorted(nums)

    assert test_res == func_res


def test_heap_sort():
    nums = rand_int_array(10, -50, 50)

    func_res = heap_sort(nums)
    test_res = sorted(nums)

    assert test_res == func_res


# Тесты стека
def test_stack_pop():
    test = Stack()

    test.push(2)
    test.push(3)
    test.push(4)

    test.pop()

    assert test.stack == [2, 3]


def test_stack_push():
    test = Stack()

    test.push(3)
    test.push(4)

    assert test.stack == [3, 4]


def test_stack_is_empty_True():
    test = Stack()

    func_res = test.is_empty()

    assert True == func_res


def test_stack_is_empty_False():
    test = Stack()

    test.push(2)
    func_res = test.is_empty()

    assert False == func_res


def test_stack_peek():
    test = Stack()

    test.push(2)
    test.push(4)

    func_res = test.peek()

    assert test.stack == [2, 4] and func_res == 4


def test_stack_len():
    test = Stack()

    test.push(2)
    test.push(3)
    test.push(4)

    func_res = len(test.stack)

    assert func_res == 3


def test_stack_min():
    test = Stack()

    test.push(4)
    test.push(7)
    test.push(2)

    func_res = test.min()

    assert func_res == 2


# Тесты фибонначи и факториала
def test_factorial():

    func_res = factorial(5)

    assert func_res == 120


def test_factorial_recursive():

    func_res = factorial_recursive(5)

    assert func_res == 120


def test_fibo():

    func_res = fibo(10)

    assert func_res == 55


def test_fibo_recursive():

    func_res = fibo_recursive(10)

    assert func_res == 55
