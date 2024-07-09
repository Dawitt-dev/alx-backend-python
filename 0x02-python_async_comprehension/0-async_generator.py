#!/usr/bin/env python3
"""Async Generator Example"""
import asyncio
import random


async def async_generator():
    """
    Async generator that loops 10 times, each
    time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    # This part won't be executed when imported as a module
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
