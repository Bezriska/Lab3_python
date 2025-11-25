import pytest
from src.sorts import (bubble_sort, quick_sort,
                       counting_sort, radix_sort, bucket_sort)
from src.heap_sort import (heap_sort)


def test_bubble_sort():
    nums = [0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]

    func_res = bubble_sort(nums)
    test_res = [-8, -4, 0, 2, 2, 6, 6, 10, 11, 21, 42]

    assert test_res == func_res


def test_quick_sort():
    nums = [0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]

    func_res = quick_sort(nums)
    test_res = [-8, -4, 0, 2, 2, 6, 6, 10, 11, 21, 42]

    assert test_res == func_res


def test_counting_sort():
    nums = [0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]

    func_res = counting_sort(nums)
    test_res = [-8, -4, 0, 2, 2, 6, 6, 10, 11, 21, 42]

    assert test_res == func_res

# пофиксить квик сорт с отр числами
# def test_radix_sort():
#     nums = [0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]

#     func_res = radix_sort(nums)
#     test_res = [-8, -4, 0, 2, 2, 6, 6, 10, 11, 21, 42]

#     assert test_res == func_res


def test_bucket_sort():
    nums = [0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]

    func_res = bucket_sort(nums)
    test_res = [-8, -4, 0, 2, 2, 6, 6, 10, 11, 21, 42]

    assert test_res == func_res


def test_heap_sort():
    nums = [0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]

    func_res = heap_sort(nums)
    test_res = [-8, -4, 0, 2, 2, 6, 6, 10, 11, 21, 42]

    assert test_res == func_res
