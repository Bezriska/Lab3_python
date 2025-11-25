def factorial(num: int):
    """Считает факториал числа

    Args:
        num (int): число, факториал которого нужно посчитать

    Returns:
        res (int): значение факториала заданного числа
    """
    if not isinstance(num, int):
        raise ValueError("Передаваемое значение должно быть типа int")

    if num == 0:
        return 0

    i = 1
    res = 1
    while i <= num:
        res *= i
        i += 1

    return res


def factorial_recursive(num: int):
    """Рекурсивно считает факториал числа

    Args:
        num (int): число, факториал которого нужно посчитать

    Returns:
        int: значение факториала заданного числа
    """
    if not isinstance(num, int):
        raise ValueError("Передаваемое значение должно быть типа int")

    if num == 0:
        return 0
    if num == 1:
        return num
    else:
        return num * factorial_recursive(num - 1)


def fibo(n: int):
    """Считает последовательность фибоначчи до заданного члена и возвращает его

    Args:
        n (int): член последовательности фибоначчи

    Returns:
        res: int: значение последнего члена заданной последвательности
    """
    if not isinstance(n, int):
        raise ValueError("Передаваемое значение должно быть типа int")

    if n == 0:
        return 0
    if n == 1:
        return 1

    i = 0
    res = 0
    past_1 = 1
    past_2 = 0
    while i < n-1:
        res = past_1 + past_2
        past_2 = past_1
        past_1 = res
        i += 1
    return res


def fibo_recursive(n: int):
    """Рекурсивно читает последовательность фибоначчи до заданного члена и возвращает его

    Args:
        n (int): член последовательности фибоначчи

    Returns:
        int: значение последнего члена заданной последвательности
    """
    if not isinstance(n, int):
        raise ValueError("Передаваемое значение должно быть типа int")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
