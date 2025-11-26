from src.sorts import type_check_float, type_check_int


def heapify(nums: list[int], n, i):
    """Сравниевает родительские и дочерние элементы, перемещает в верх кучи наибольший эл-т

    Args:
        nums (list[int]): список для сортировки
        n (int): кол-во элементов списка (длина)
        i (int): наибольший эл-т
    """

    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and nums[left] > nums[largest]:
        largest = left

    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heap_sort(a: list[int]) -> list[int]:
    """Сортировка кучей по возрастанию

    Args:
        a (list[int]): список, который нужно отсортировать

    Returns:
        list[int]: отсортированный по возрастанию список
    """

    if not a:
        raise ValueError("Передан пустой список")

    if not type_check_int(a):
        raise ValueError("Все элементы списка должны быть типа 'int'")

    nums = a[:]

    n = len(nums)

    for i in range(n // 2, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

    return nums
