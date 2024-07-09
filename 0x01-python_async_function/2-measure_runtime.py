#!/usr/bin/env python3
"""Measure the runtime"""
import time
import asyncio
import importlib

# Dynamically import the wait_n function from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time

    Parameters:
    n (int): Number of times to spawn wait_random.
    max_delay (int): Maximum delay for wait_random.

    Returns:
    float: Average time per call.
    """
    start_time = time.perf_counter()  # Start the timer
    asyncio.run(wait_n(n, max_delay))  # Execute the wait_n function
    end_time = time.perf_counter()  # End the timer
    total_time = end_time - start_time  # Calculate the total time
    return total_time / n  # Return the average time per call


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
