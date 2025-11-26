from src.INFO import algos, arrays, sorts
from src.sorts import (bubble_sort, quick_sort,
                       counting_sort, radix_sort, bucket_sort)
from src.heap_sort import (heap_sort)
from src.stack import Stack
from src.fibonacci_and_factorial import fibo, fibo_recursive, factorial, factorial_recursive


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    stop_word = "kill"
    while True:
        print("Для вывода доступных алгоритмов, сортировок и генераторов введите: 'help'")
        user_input = input("Введите интересующее вас название: ")

        if user_input == "help":
            print("Алгоритмы:")
            for alg in algos:
                print(alg)

            print("\nСортировки:")
            for sort in sorts:
                print(sort)

            print("\nГенераторы:")
            for gen in arrays:
                print(gen)

        elif user_input == "factorial":
            value = input("Какое значение хотите передать в функцию (int): ")

            print(factorial(int(value)), "\n")

        elif user_input == "factorial_recursive":
            value = input("Какое значение хотите передать в функцию (int): ")

            print(factorial_recursive(int(value)), "\n")

        elif user_input == "fibo":
            value = input("Какое значение хотите передать в функцию (int): ")

            print(fibo(int(value)), "\n")

        elif user_input == "fibo_recursive":
            value = input("Какое значение хотите передать в функцию (int): ")

            print(fibo_recursive(int(value)), "\n")

        elif user_input == stop_word:
            break


if __name__ == "__main__":
    main()
