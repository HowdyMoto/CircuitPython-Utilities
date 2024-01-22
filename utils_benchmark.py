import time
import random

# Number of operations
NUM_OPERATIONS = 100000000


# Function to benchmark integer math
def int_math(num_operations):
    int_random1 = random.randint(0,1000)
    int_random2 = random.randint(0,1000)
    start_time = time.time()
    result = 0
    
    for _ in range(num_operations):
        result += int_random1
        result -= int_random2

    end_time = time.time()
    return end_time - start_time

# Function to benchmark floating point math
def float_math(num_operations):
    float_random1 = random.uniform(1.0,1000.0)
    float_random2 = random.uniform(1.0,1000.0)
    start_time = time.time()

    result = 0.0
    for _ in range(num_operations):
        result += float_random1
        result -= float_random1

    end_time = time.time()
    return end_time - start_time



# Benchmarking
time_int = int_math(NUM_OPERATIONS)
time_float = float_math(NUM_OPERATIONS)

print(f"Time taken for integer math: {time_int} seconds")
print(f"Time taken for floating-point math: {time_float} seconds")