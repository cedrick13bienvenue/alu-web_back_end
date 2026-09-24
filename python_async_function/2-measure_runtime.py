#!/usr/bin/env python3
"""Module for measuring the runtime of concurrent coroutines."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime of wait_n(n, max_delay)."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
