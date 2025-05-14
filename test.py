import sys
from pathlib import Path
build_dir = Path(__file__).parent / 'build'
sys.path.append(str(build_dir))

import pymodule

# Create an instance of TestCalculator
calculator = pymodule.TestCalculator()

# Test sum_to_n with different values
print("\nTesting sum_to_n:")
print(f"Sum from 1 to 5: {calculator.sum_to_n(5)}")  # Should print 15
print(f"Sum from 1 to 10: {calculator.sum_to_n(10)}")  # Should print 55
print(f"Sum from 1 to 0: {calculator.sum_to_n(0)}")  # Should print 0

# Test multiply_to_n with different values
print("\nTesting multiply_to_n:")
print(f"Multiply from 1 to 5: {calculator.multiply_to_n(5)}")  # Should print 120 (5!)
print(f"Multiply from 1 to 3: {calculator.multiply_to_n(3)}")  # Should print 6 (3!)
print(f"Multiply from 1 to 0: {calculator.multiply_to_n(0)}")  # Should print 0

# Test with negative number (should raise ValueError)
print("\nTesting error handling:")
try:
    calculator.sum_to_n(-1)
except ValueError as e:
    print("Successfully caught ValueError for negative input in sum_to_n")

try:
    calculator.multiply_to_n(-1)
except ValueError as e:
    print("Successfully caught ValueError for negative input in multiply_to_n")

def multiply_to_n(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * multiply_to_n(n - 1) if n > 0 else 1

# start a timer
import time

NUMBER_TO_TEST = 20

# Test Python multiply_to_n with a timer
start_time = time.time()
print("\nTesting multiply_to_n:")
print(multiply_to_n(NUMBER_TO_TEST))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

# Test pymodule calculator.multiply_to_n with a timer
import time
start_time = time.time()
print("\nTesting pymodule:")
print(calculator.multiply_to_n(NUMBER_TO_TEST))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")





# print("\nTesting sum of squares implementations:")
# import threading
# import multiprocessing
# import time
# import numpy as np
# from concurrent.futures import ThreadPoolExecutor
# from functools import partial

# # Parameters for the test
# RANGE_SIZE = 100_000_000
# num_threads = multiprocessing.cpu_count()

# # Pure Python implementation
# def calculate_square(x):
#     return x * x

# start_time = time.perf_counter_ns()
# pure_python_result = sum(calculate_square(i) for i in range(RANGE_SIZE))
# end_time = time.perf_counter_ns()
# print(f"\nPure Python Result: {pure_python_result}")
# print(f"Pure Python Time: {(end_time - start_time)/1000000} milliseconds")

# # Threading implementation
# def thread_worker(start, end):
#     return sum(i * i for i in range(start, end))

# start_time = time.perf_counter_ns()
# chunk_size = RANGE_SIZE // num_threads
# futures = []

# with ThreadPoolExecutor(max_workers=num_threads) as executor:
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = start + chunk_size if i < num_threads - 1 else RANGE_SIZE
#         futures.append(executor.submit(thread_worker, start, end))

# threaded_result = sum(f.result() for f in futures)
# end_time = time.perf_counter_ns()
# print(f"\nThreaded Result: {threaded_result}")
# print(f"Threading Time: {(end_time - start_time)/1000000} milliseconds")

# # Multiprocessing implementation
# def process_worker(chunk):
#     start, end = chunk
#     return sum(i * i for i in range(start, end))

# if __name__ == "__main__":
#     start_time = time.perf_counter_ns()
#     chunks = [(i * chunk_size, (i + 1) * chunk_size if i < num_threads - 1 else RANGE_SIZE) 
#              for i in range(num_threads)]
    
#     with multiprocessing.Pool(processes=num_threads) as pool:
#         results = pool.map(process_worker, chunks)
    
#     multiprocess_result = sum(results)
#     end_time = time.perf_counter_ns()
#     print(f"\nMultiprocessing Result: {multiprocess_result}")
#     print(f"Multiprocessing Time: {(end_time - start_time)/1000000} milliseconds")
