import random


def rand_int_array(n: int, lo: int, hi: int, distinct=False, seed=None) -> list[int]:
    """Генерирует список из рандомных целочисленных значений

    Args:
        n (int): кол-во элементов списка (длина)
        lo (int): минимальное значение
        hi (int): максимальное значение
        distinct (bool, optional): обязательно ли все значения должны быть разными. По умолчанию False.
        seed (int, optional): сид генератора. По умолчанию None.

    Raises:
        ValueError: Невозможно сгенерировать уникальные значения в диапазоне

    Returns:
        list[int]: список из рандомных целочисленных значений
    """
    if seed is not None:
        random.seed(seed)

    rand = []

    if distinct:
        if n > (hi - lo + 1):
            raise ValueError(
                f"Невозможно сгенерировать уникальные значения в диапазоне {lo}:{hi}")
        rand = random.sample(range(lo, hi + 1), n)
    else:
        for _ in range(n):
            rand.append(random.randint(lo, hi))

    return rand


def nearly_sorted(n: int, swaps: int, seed=None) -> list[int]:
    """Генерирует отсортированный список с некоторым количеством перестановок

    Args:
        n (int): кол-во элементов списка (длина)
        swaps (int): кол-во перестановок
        seed (int, optional): сид генератора. По умолчаню None.

    Returns:
        list[int]: отсортированный список с некоторым количеством перестановок
    """
    if seed is not None:
        random.seed(seed)

    lst = []
    for _ in range(n):
        lst.append(random.randint(-2*n, 2*n))
    lst.sort()

    swap_ind = []
    for _ in range(swaps):
        i = 0
        ind = []
        while i < 2:
            ind.append(random.randint(0, n-1))
            i += 1
        swap_ind.append(ind)

    j = 0
    while j < len(swap_ind):
        lst[swap_ind[j][0]], lst[swap_ind[j][1]
                                 ] = lst[swap_ind[j][1]], lst[swap_ind[j][0]]
        j += 1

    return lst


def many_duplicates(n: int, k_unique=5, seed=None) -> list[int]:
    """Генерирует список, состоящий из одинаковых целочесленных элементов с
    некоторым количеством уникальных

    Args:
        n (int): кол-во элементов списка (длина)
        k_unique (int, optional): кол-во уникальных элементов. По умолчанию 5.
        seed (int, optional): сид генератора. По умолчанию None.

    Returns:
        list: список, состоящий из одинаковых целочесленных элементов с
    некоторым количеством уникальных
    """

    if seed is not None:
        random.seed(seed)

    duplicate_value = random.randint(-2*n, 2*n)
    lst = [duplicate_value] * n

    available_range = [x for x in range(-2*n, 2*n) if x != duplicate_value]
    rand_nums = random.sample(available_range, k_unique)

    positions = random.sample(range(n), k_unique)

    for i in range(k_unique):
        lst[positions[i]] = rand_nums[i]

    return lst


def reverse_sorted(n: int) -> list[int]:
    """Генерирует отсортированный по убываню список из целочисленых значений

    Args:
        n (int): кол-во элементов списка (длина)

    Returns:
        list[int]: Отсортированный по убыванию список
    """

    rand_lst = [random.randint(-2*n, 2*n) for _ in range(n)]

    rand_lst.sort(reverse=True)
    return rand_lst


def rand_float_array(n: int, lo=0.0, hi=1.0, seed=None) -> list[float]:
    """Генерирует список из рандомных вещественных значений

    Args:
        n (int): кол-во элементов списка (длина)
        lo (float, optional): минимальное значение. По умолчанию 0.0.
        hi (float, optional): максимальное значение. По умолчанию 1.0.
        seed (int, optional): сид генератора. По умолчанию None.

    Returns:
        list[float]: список из рандомных вещественных значений
    """

    if seed is not None:
        random.seed(seed)

    rand_lst = [random.uniform(lo, hi) for _ in range(n)]

    return rand_lst
