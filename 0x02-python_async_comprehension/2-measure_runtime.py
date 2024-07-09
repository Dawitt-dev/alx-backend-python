#!/usr/bin/env python3
"""Measure Runtime Example"""
import asyncio
import time
from importlib import import_module
from typing import List

# Import async_comprehension from the previous task
asyn_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel
    using asyncio.gather and measure the total runtime.

    Returns:
    float: Total runtime.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(asyn_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    async def main() -> None:
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime}")

    asyncio.run(main())
