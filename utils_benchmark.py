# By @howdymoto / Wright Bagwell
# Inspired by TodBot's circuitpython-tricks: https://github.com/todbot/circuitpython-tricks
# And by Adafruit/Kattni Rembor's CircuitPython Essentials: https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials
# MIT license
""" Helper functions for learning about your boards """

import time
import random

# How many iterations to perform. On a microcontroller, performance almost never varies, so brief tests are fine.
NUM_OPERATIONS = 1000000

# Function to benchmark integer math
def int_math():
    """Benchmark integer addition and subtraction operations.

    Performs NUM_OPERATIONS (1 million) integer math operations using
    random integers and measures execution time.

    Returns:
        float: Elapsed time in seconds.
    """
    print("\tPerforming", NUM_OPERATIONS, "integer math operations")

    int_random1 = random.randint(0,1000)
    int_random2 = random.randint(0,1000)
    start_time = time.monotonic()
    result = 0

    for _ in range(NUM_OPERATIONS):
        result += int_random1
        result -= int_random2

    end_time = time.monotonic()
    return end_time - start_time

# Function to benchmark floating point math
def float_math():
    """Benchmark floating-point addition and subtraction operations.

    Performs NUM_OPERATIONS (1 million) floating-point math operations
    using random floats and measures execution time.

    Returns:
        float: Elapsed time in seconds.
    """
    print("\tPerforming", NUM_OPERATIONS, "float math operations")

    float_random1 = random.uniform(1.0,1000.0)
    float_random2 = random.uniform(1.0,1000.0)
    start_time = time.monotonic()
    result = 0.0

    for _ in range(NUM_OPERATIONS):
        result += float_random1
        result -= float_random2

    end_time = time.monotonic()
    return end_time - start_time

# Benchmarking
def run_benchmark():
    """Run integer and floating-point math benchmarks and print results.

    Executes both int_math() and float_math() benchmarks, then prints
    the execution times. Useful for comparing performance across different
    CircuitPython boards.
    """
    print("Running math benchmark...")

    time_int = int_math()
    time_float = float_math()

    print(f"\tInteger math: {time_int} seconds")
    print(f"\tTime taken for floating-point math: {time_float} seconds")
