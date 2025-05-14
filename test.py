# # in case the module is not installed, just present in the 'build' directory:
# import sys
# from pathlib import Path
# build_dir = Path(__file__).parent / 'build'
# sys.path.append(str(build_dir))

import pymodule


print("\nTesting sum of numbers implementations:")
import threading
import multiprocessing
import time
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from functools import partial


# Parameters for the test
RANGE_SIZE = 100_000_000
num_threads = multiprocessing.cpu_count()


if __name__ == "__main__":


    # Create an instance of TestCalculator
    calculator = pymodule.TestCalculator()

    # Test sum_to_n with different values
    print("\nTesting sum_to_n:")
    print(f"Sum from 1 to 5 (15): {calculator.sum_to_n(5)}")  # Should print 15
    print(f"Sum from 1 to 10 (55): {calculator.sum_to_n(10)}")  # Should print 55
    print(f"Sum from 1 to 0 (0): {calculator.sum_to_n(0)}")  # Should print 0
    

    # Test sum_to_n with different values
    print("\nTesting sum_to_n_threaded:")
    print(f"Sum from 1 to 500 (125250): {calculator.sum_to_n_threaded(500)}")  # Should print 125250
    print(f"Sum from 1 to 1000 (500500): {calculator.sum_to_n_threaded(1000)}")  # Should print 500500
    print(f"Sum from 1 to 0 (0): {calculator.sum_to_n_threaded(0)}")  # Should print 0
    

    # Test multiply_to_n with different values
    print("\nTesting multiply_to_n:")
    print(f"Multiply from 1 to 5 (120): {calculator.multiply_to_n(5)}")  # Should print 120 (5!)
    print(f"Multiply from 1 to 3 (6): {calculator.multiply_to_n(3)}")  # Should print 6 (3!)
    print(f"Multiply from 1 to 0 (0): {calculator.multiply_to_n(0)}")  # Should print 0

    # Test multiply_to_n with different values
    print("\nTesting multiply_to_n:")
    print(f"Multiply from 1 to 20 (2432902008176640000): {calculator.multiply_to_n_threaded(20)}")  # Should print 2432902008176640000 (20!)
    print(f"Multiply from 1 to 10 (3628800): {calculator.multiply_to_n_threaded(10)}")  # Should print 3628800 (10!)
    print(f"Multiply from 1 to 0 (0): {calculator.multiply_to_n_threaded(0)}")  # Should print 0

    # Test with negative number (should raise ValueError)
    print("\nTesting error handling:")
    try:
        calculator.sum_to_n(-1)
    except ValueError as e:
        print("Successfully caught ValueError for negative input in sum_to_n")

    try:
        calculator.sum_to_n_threaded(-1)
    except ValueError as e:
        print("Successfully caught ValueError for negative input in sum_to_n_threaded")

    try:
        calculator.multiply_to_n(-1)
    except ValueError as e:
        print("Successfully caught ValueError for negative input in multiply_to_n")

    try:
        calculator.multiply_to_n_threaded(-1)
    except ValueError as e:
        print("Successfully caught ValueError for negative input in multiply_to_n_threaded")

    def multiply_to_n(n):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        return n * multiply_to_n(n - 1) if n > 0 else 1


    print("\n\nBasic tests for multiply_to_n comparing with pure Python:")
    NUMBER_TO_TEST = 20

    # Test Python multiply_to_n with a timer
    start_time = time.perf_counter_ns()
    print("\nTesting multiply_to_n (pure Python):")
    print(multiply_to_n(NUMBER_TO_TEST))
    end_time = time.perf_counter_ns()
    print(f"Time taken: {(end_time - start_time)/1_000} microseconds")

    # Test pymodule calculator.multiply_to_n with a timer
    start_time = time.perf_counter_ns()
    print("\nTesting pymodule (C++ module, no multiprocessing nor multithreading):")
    print(calculator.multiply_to_n(NUMBER_TO_TEST))
    end_time = time.perf_counter_ns()
    print(f"Time taken: {(end_time - start_time)/1_000} microseconds")

    # Test pymodule calculator.multiply_to_n_threaded with a timer
    start_time = time.perf_counter_ns()
    print("\nTesting pymodule (C++ module, multithreading):")
    print(calculator.multiply_to_n_threaded(NUMBER_TO_TEST))
    end_time = time.perf_counter_ns()
    print(f"Time taken: {(end_time - start_time)/1_000} microseconds")


    print("\n\nImproved tests for sum_to_n comparing with pure Python, Python's multiprocessing, Python's multitasking and pymodule's threading implementations:")

    # Pure Python implementation
    start_time = time.perf_counter_ns()
    pure_python_result = sum(i for i in range(RANGE_SIZE))
    end_time = time.perf_counter_ns()
    print(f"\nPure Python Result: {pure_python_result}")
    print(f"Pure Python Time: {(end_time - start_time)/1000000} milliseconds")

    # Threading implementation
    def thread_worker(start, end):
        return sum(i for i in range(start, end))

    start_time = time.perf_counter_ns()
    chunk_size = RANGE_SIZE // num_threads
    futures = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start = i * chunk_size
            end = start + chunk_size if i < num_threads - 1 else RANGE_SIZE
            futures.append(executor.submit(thread_worker, start, end))

    threaded_result = sum(f.result() for f in futures)
    end_time = time.perf_counter_ns()
    print(f"\nThreaded Result: {threaded_result}")
    print(f"Threading Time: {(end_time - start_time)/1000000} milliseconds")

    # Multiprocessing implementation
    def process_worker(chunk):
        start, end = chunk
        return sum(i for i in range(start, end))


    start_time = time.perf_counter_ns()
    chunks = [(i * chunk_size, (i + 1) * chunk_size if i < num_threads - 1 else RANGE_SIZE) 
             for i in range(num_threads)]
    
    with multiprocessing.Pool(processes=num_threads) as pool:
        results = pool.map(process_worker, chunks)
    
    multiprocess_result = sum(results)
    end_time = time.perf_counter_ns()
    print(f"\nMultiprocessing Result: {multiprocess_result}")
    print(f"Multiprocessing Time: {(end_time - start_time)/1000000} milliseconds")

    # C++ module implementation
    start_time = time.perf_counter_ns()
    result = calculator.sum_to_n(RANGE_SIZE-1)
    end_time = time.perf_counter_ns()
    print(f"\nC++ Module Result (no multiprocessing nor multithreading): {result}")
    print(f"C++ Module Time: {(end_time - start_time)/1000000} milliseconds")

    start_time = time.perf_counter_ns()
    result = calculator.sum_to_n_threaded(RANGE_SIZE-1)
    end_time = time.perf_counter_ns()
    print(f"\nC++ Module Result (multithreading): {result}")
    print(f"C++ Module Time: {(end_time - start_time)/1000000} milliseconds")
