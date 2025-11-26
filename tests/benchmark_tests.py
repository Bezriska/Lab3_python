from src.benchmarks import benchmark_sorts
from src.heap_sort import heap_sort
from src.sorts import (bubble_sort, counting_sort, quick_sort, bucket_sort,
                       radix_sort)
from src.generators import (rand_int_array, rand_float_array, nearly_sorted,
                            many_duplicates, reverse_sorted)


arrays = dict()
algos = dict()

arrays = {
    "random_int": rand_int_array(10, -100, 100),
    # "random_float": rand_float_array(10), # Не работает с counting_sort и radix_sort
    "nearly_sorted": nearly_sorted(10, 4),
    "many_duplicates": many_duplicates(10),
    "reverse_sorted": reverse_sorted(10)
}

algos = {
    "bubble_sort": bubble_sort,
    "counting_sort": counting_sort,
    "quick_sort": quick_sort,
    "bucket_sort": bucket_sort,
    "radix_sort": radix_sort,
    "heap_sort": heap_sort
}

result = benchmark_sorts(arrays, algos)

for algo, times in result.items():
    print(f"\n{algo}:")
    for arr_name, time_val in times.items():
        print(f"  {arr_name}: {time_val:.7f}")
