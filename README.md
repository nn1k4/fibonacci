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

To run the code in this repository, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. If the `venv` directory doesn't exist in the project's root directory, create a virtual environment by running the following command:

    ```
    python -m venv venv
    ```

3. Activate the virtual environment by running the following command: 

    ```
    venv\Scripts\activate
    ```

You should see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

4. Once the virtual environment is activated, run the code using the following command:

    ```
    python -m test
    ```

This command will execute the `test` module, which corresponds to the `test.py` file in the project directory.

5. After running the code, you can deactivate the virtual environment by running the following command:

    ```
    venv\Scripts\deactivate
    ```
This will return you to your normal command prompt.

Note: Make sure you have the necessary dependencies installed in your virtual environment before running the code. If you encounter any missing dependencies, you can install them using `pip install <package-name>` while the virtual environment is active.


## Dependencies

The program requires numpy for matrix operations and time for measuring execution time.