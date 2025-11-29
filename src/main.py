from src.INFO import algos, arrays, sorts
from src.sorts import (bubble_sort, quick_sort,
                       counting_sort, radix_sort, bucket_sort)
from src.heap_sort import heap_sort
from src.stack import Stack
from src.fibonacci_and_factorial import fibo, fibo_recursive, factorial, factorial_recursive
from src.generators import (rand_int_array, rand_float_array, nearly_sorted,
                            many_duplicates, reverse_sorted)


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    stop_word = "kill"
    while True:
        print("Для вывода доступных алгоритмов, сортировок и генераторов введите: 'help'")
        print("Для выхода введите: 'kill'")
        user_input = input("Введите интересующее вас название: ").strip()

        if user_input == "help":
            print("\nАлгоритмы:")
            for alg in algos:
                print(f"  - {alg}")

            print("\nСортировки:")
            for sort in sorts:
                print(f"  - {sort}")
            print("  - heap_sort")

            print("\nГенераторы:")
            for gen in arrays:
                print(f"  - {gen}")

            print("\nСтруктуры данных:")
            print("  - stack")

        # Алгоритмы
        elif user_input == "factorial":
            try:
                value = input(
                    "Какое значение хотите передать в функцию (int): ")
                print(f"Результат: {factorial(int(value))}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "factorial_recursive":
            try:
                value = input(
                    "Какое значение хотите передать в функцию (int): ")
                print(f"Результат: {factorial_recursive(int(value))}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "fibo":
            try:
                value = input(
                    "Какое значение хотите передать в функцию (int): ")
                print(f"Результат: {fibo(int(value))}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "fibo_recursive":
            try:
                value = input(
                    "Какое значение хотите передать в функцию (int): ")
                print(f"Результат: {fibo_recursive(int(value))}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        # Сортировки
        elif user_input == "bubble_sort":
            try:
                arr_str = input(
                    "Введите числа через пробел (например: 5 2 8 1 9): ")
                arr = [int(x) for x in arr_str.split()]
                result = bubble_sort(arr)
                print(f"Отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "quick_sort":
            try:
                arr_str = input(
                    "Введите числа через пробел (например: 5 -2 8 1 -9): ")
                arr = [int(x) for x in arr_str.split()]
                result = quick_sort(arr)
                print(f"Отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "counting_sort":
            try:
                arr_str = input("Введите целые числа через пробел: ")
                arr = [int(x) for x in arr_str.split()]
                result = counting_sort(arr)
                print(f"Отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "radix_sort":
            try:
                arr_str = input("Введите целые числа через пробел: ")
                arr = [int(x) for x in arr_str.split()]
                result = radix_sort(arr)
                print(f"Отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "bucket_sort":
            try:
                arr_str = input(
                    "Введите вещественные числа через пробел (например: 0.5 0.2 0.8): ")
                arr = [float(x) for x in arr_str.split()]
                result = bucket_sort(arr)
                print(f"Отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "heap_sort":
            try:
                arr_str = input("Введите числа через пробел: ")
                arr = [int(x) for x in arr_str.split()]
                result = heap_sort(arr)
                print(f"Отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        # Генераторы
        elif user_input == "random_int":
            try:
                n = int(input("Количество элементов: "))
                lo = int(input("Минимальное значение: "))
                hi = int(input("Максимальное значение: "))
                distinct = input("Уникальные элементы? (y/n): ").lower() == 'y'
                result = rand_int_array(n, lo, hi, distinct=distinct)
                print(f"Сгенерированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "random_float":
            try:
                n = int(input("Количество элементов: "))
                lo = float(
                    input("Минимальное значение (по умолчанию 0.0): ") or 0.0)
                hi = float(
                    input("Максимальное значение (по умолчанию 1.0): ") or 1.0)
                result = rand_float_array(n, lo, hi)
                print(f"Сгенерированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "nearly_sorted":
            try:
                n = int(input("Количество элементов: "))
                swaps = int(input("Количество обменов: "))
                result = nearly_sorted(n, swaps)
                print(f"Почти отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "many_duplicates":
            try:
                n = int(input("Количество элементов: "))
                k_unique = int(
                    input("Количество уникальных значений (по умолчанию 5): ") or 5)
                result = many_duplicates(n, k_unique)
                print(f"Массив с дубликатами: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        elif user_input == "reverse_sorted":
            try:
                n = int(input("Количество элементов: "))
                result = reverse_sorted(n)
                print(f"Обратно отсортированный массив: {result}\n")
            except Exception as e:
                print(f"Ошибка: {e}\n")

        # Стек
        elif user_input == "stack":
            print("\nИнтерактивная работа со стеком")
            stack = Stack()
            while True:
                print("\nКоманды: push, pop, peek, min, len, is_empty, show, exit")
                cmd = input("Введите команду: ").strip().lower()

                if cmd == "push":
                    try:
                        value = int(input("Введите значение: "))
                        stack.push(value)
                        print(f"Добавлено: {value}")
                    except Exception as e:
                        print(f"Ошибка: {e}")

                elif cmd == "show":
                    print(stack.stack)

                elif cmd == "pop":
                    try:
                        value = stack.pop()
                        print(f"Извлечено: {value}")
                    except Exception as e:
                        print(f"Ошибка: {e}")

                elif cmd == "peek":
                    try:
                        value = stack.peek()
                        print(f"Верхний элемент: {value}")
                    except Exception as e:
                        print(f"Ошибка: {e}")

                elif cmd == "min":
                    try:
                        value = stack.min()
                        print(f"Минимальный элемент: {value}")
                    except Exception as e:
                        print(f"Ошибка: {e}")

                elif cmd == "len":
                    print(f"Размер стека: {len(stack.stack)}")

                elif cmd == "is_empty":
                    print(f"Стек пуст: {stack.is_empty()}")

                elif cmd == "exit":
                    break

                else:
                    print("Неизвестная команда")

        elif user_input == stop_word:
            print("Выход из программы...")
            break

        else:
            print(
                f"Неизвестная команда: '{user_input}'. Введите 'help' для справки.")


if __name__ == "__main__":
    main()
