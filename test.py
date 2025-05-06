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
