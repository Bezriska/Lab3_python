import time
from typing import Callable


def temeit_once(func, *args, **kwargs):

    start = time.perf_counter()
    func(*args, **kwargs)
    stop = time.perf_counter()

    res = stop - start
    return res


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    result_dict = dict()

    for i in algos.keys():
        time_dict = dict()
        for j in arrays.keys():

            time = temeit_once(algos[i], arrays[j])
            time_dict[j] = time

        result_dict[i] = time_dict

    return result_dict
