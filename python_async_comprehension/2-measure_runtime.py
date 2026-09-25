#!/usr/bin/env python3
"""Module for measuring the runtime of parallel async comprehensions."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension 4 times in parallel and return the runtime."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
