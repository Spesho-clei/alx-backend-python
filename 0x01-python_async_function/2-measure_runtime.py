#!/usr/bin/env python3

""" task 2 module """

import asyncio
from time import perf_counter
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Total execution time divided by n.
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = perf_counter()

    total_time = end_time - start_time
    average_time_per_task = total_time / n

    return average_time_per_task
