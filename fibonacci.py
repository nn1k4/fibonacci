import numpy as np
import os
import sys
import time

def fibonacci(n):
    F = np.array([[1, 1], [1, 0]], dtype=object)
    if n == 0:
        return 0
    power = np.linalg.matrix_power(F, n - 1)
    return power[0][0]

def main():
    n = int(input("Enter a positive integer: "))
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    execution_time = end_time - start_time
    sys.set_int_max_str_digits(2147483647)  # Increase the maximum number of digits to 2147483647
    result_str = f"Execution time: {execution_time} seconds\nFibonacci number at position {n} is {result}"

    if os.path.exists("result.txt"):
        print("File 'result.txt' already exists. Do you want to overwrite it? (y/n)")
        answer = input().lower()
        if answer != "y":
            print("Program is terminating.")
            sys.exit()

    with open("result.txt", "w", encoding='utf-8') as f:
        f.write(result_str)

    print(result_str)

if __name__ == "__main__":
    main()