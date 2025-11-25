def bubble_sort(a: list[int]) -> list[int]:
    """Пузырьковая сортировка по возрастанию

    Args:
        a (list[int]): список, который нужно отсортировать по возрастанию

    Returns:
        list[int]: отсортированный список
    """
    if len(a) == 0:
        raise ValueError("Передан пустой список")

    num = a[:]
    for i in range(len(num)-1):
        j = 1
        while j < len(num):
            k = j - 1
            if num[k] > num[j]:
                num[k], num[j] = num[j], num[k]
                j += 1
            else:
                j += 1
    return num


def quick_sort(a: list[int]) -> list[int]:
    """Сортировка по возрастанию с помощью метода quicksort

    Args:
        a (list[int]): список, который нужно отсортировать

    Returns:
        list[int]: отсорированный список
    """
    nums = a[:]
    j = 1
    i = 0

    if len(nums) < 2:
        return nums
    elif len(nums) == 2:
        if nums[j] < nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        return nums
    else:
        pivot = nums[0]
        del nums[0]

        j = 0
        i = -1

        while j < len(nums):
            if nums[j] >= pivot:
                j += 1
            else:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        right = nums[i+1:]
        left = nums[:i+1]
    return quick_sort(left) + [pivot] + quick_sort(right)


def counting_sort(a: list[int]) -> list[int]:
    """Сортировка по возрастанию методом counting sort

    Args:
        a (list[int]): список, который нужно отсортировать

    Returns:
        list[int]: отсортированный список
    """
    if len(a) == 0:
        raise ValueError("Передан пустой список")

    mn = min(a)
    mx = max(a)
    nums_quantity = mx - mn + 1

    c = []
    for _ in range(nums_quantity):
        c.append(0)

    for i in range(len(a)):

        c[a[i]-mn] += 1

    output = []
    i = 0
    while i < nums_quantity:
        if c[i] > 0:
            for k in range(c[i]):
                output.append(i + mn)
        i += 1

    return output

# Пофиксить отрицательные числа в radix_sort()


def radix_sort(a: list[int], base=10) -> list[int]:
    """Сортировка по возрастанию методом radix sort

    Args:
        a (list[int]): список, который нужно отсортировать

    Returns:
        list[int]: отсортированный список
    """
    if len(a) == 0:
        raise ValueError("Передан пустой список")

    nums = a[:]
    mx = len(str(max(nums)))

    interm = [[] for _ in range(base)]

    for i in range(0, mx):
        for j in nums:
            digit = (j // base ** i) % base
            interm[digit].append(j)

        nums = [x for queue in interm for x in queue]

        interm = [[] for _ in range(base)]

    return nums


def bucket_sort(a: list[int], bucket_count: int | None = None) -> list[int]:
    nums = a[:]

    mn = min(nums)
    mx = max(nums)

    if bucket_count == None:
        bucket_count = len(nums)

    buckets = [[] for _ in range(bucket_count)]

    for num in nums:
        index = int((num - mn) / (mx - mn + 1) * bucket_count)
        buckets[index].append(num)

    sorted_list = []
    for bucket in buckets:
        if bucket == []:
            continue
        else:
            sorted_list.extend(quick_sort(bucket))

    return sorted_list


print(radix_sort([0, 2, -4, 6, 2, -8, 6, 10, 42, 11, 21]))
