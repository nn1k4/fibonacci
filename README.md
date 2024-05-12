# Fibonacci

This Python program calculates the Fibonacci number at a given position using matrix exponentiation, which makes it efficient for large inputs.

## How it Works

The program consists of two main functions: `fibonacci(n)` and `main()`.

### fibonacci(n)

This function calculates the Fibonacci number at position `n`. It uses a 2x2 matrix [[1, 1], [1, 0]], which is raised to the power of (n-1) using numpy's `linalg.matrix_power` function. If `n` is 0, the function returns 0. Otherwise, it returns the element at position [0][0] of the resulting matrix, which is the Fibonacci number at position `n`.

### main()

This function is the entry point of the program. It prompts the user to enter a positive integer, which is passed to the `fibonacci(n)` function. The function measures the execution time of the `fibonacci(n)` function and stores the result. 

The result, along with the execution time, is then written to a file named "result.txt". If the file already exists, the program asks the user if they want to overwrite it. If the user answers anything other than "y", the program terminates.

## How to Run

To run the program, simply execute the `fibonacci.py` script with Python 3. You will be prompted to enter a positive integer, and the result will be written to "result.txt" in the same directory.

## Dependencies

The program requires numpy for matrix operations and time for measuring execution time.