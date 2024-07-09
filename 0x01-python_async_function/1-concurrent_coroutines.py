#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Parameters:
    n (int): Number of times to spawn wait_random.
    max_delay (int): Maximum delay for wait_random.

    Returns:
    List[float]: List of delays in ascending order.
    """
    # Create a list of tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Run tasks concurrently and collect the results
    delays = await asyncio.gather(*tasks)
    # Return the list of delays in ascending order
    return sorted(delays)

if __name__ == "__main__":
    # Test the wait_n function
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
