#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds.

    Parameters:
    max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
    float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)  # Generate random delay
    await asyncio.sleep(delay)            # Wait for the delay
    return delay                          # Return the delay


if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
