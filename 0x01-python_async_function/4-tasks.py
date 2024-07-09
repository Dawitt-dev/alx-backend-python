#!/usr/bin/env python3
"""Function that executes multiple tasks concurrently"""
import asyncio
from typing import List
from importlib import import_module

# Import task_wait_random from 3-tasks.py
task_wait_random = import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Parameters:
    n (int): Number of times to spawn task_wait_random.
    max_delay (int): Maximum delay for task_wait_random.

    Returns:
    List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)  # Return the list of delays in ascending order

if __name__ == "__main__":
    # Test the task_wait_n function
    print(asyncio.run(task_wait_n(5, 5)))
    print(asyncio.run(task_wait_n(10, 7)))
    print(asyncio.run(task_wait_n(10, 0)))
