from src.benchmarks import benchmark_sorts, temeit_once
from src.heap_sort import heap_sort
from src.sorts import (bubble_sort, counting_sort, quick_sort, bucket_sort,
                       radix_sort)
from src.generators import (rand_int_array, rand_float_array, nearly_sorted,
                            many_duplicates, reverse_sorted)


arrays = dict()
algos = dict()

arrays = {
    "random_int": rand_int_array(10, -100, 100),
    # "random_float": rand_float_array(10), # Работает только с bucket_sort()
    "nearly_sorted": nearly_sorted(10, 4),
    "many_duplicates": many_duplicates(10),
    "reverse_sorted": reverse_sorted(10)
}

algos = {
    "bubble_sort": bubble_sort,
    "counting_sort": counting_sort,
    "quick_sort": quick_sort,
    # "bucket_sort": bucket_sort, # Работает только с float
    "radix_sort": radix_sort,
    "heap_sort": heap_sort
}

result = benchmark_sorts(arrays, algos)

for algo, times in result.items():
    print(f"\n{algo}:")
    for arr_name, time_val in times.items():
        print(f"  {arr_name}: {time_val:.7f}")

print("\nТест bucket_sort")
print("Отсортированный массив:", bucket_sort(rand_float_array(10)))
print("Затраченное время:",
      f"{temeit_once(bucket_sort, rand_float_array(10)):.7f}")
