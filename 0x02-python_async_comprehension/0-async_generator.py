#!/usr/bin/env python3

""" task 0 module """

import asyncio
import random

async def async_generator():
    """
    Coroutine that loops 10 times, waits 1 second asynchronously
    each time, and yields a random number between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
