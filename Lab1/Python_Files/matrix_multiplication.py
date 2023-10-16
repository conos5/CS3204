import numpy as np
import time
import matplotlib.pyplot as plt


def matrix_multiply(num):
    # Generate random matrices A and B of size n x n
    start_time = time.perf_counter()
    A = np.random.rand(num, num)
    B = np.random.rand(num, num)

    # Measure the execution time of matrix multiplication
    result = np.matmul(A, B)
    end_time = time.perf_counter()

    return end_time - start_time


if __name__ == '__main__':
    matrix_sizes = [1000, 3000, 5000, 7500, 8500, 9000, 10000, 11000, 12000]  # Adjust as needed
    execution_times = []

    for n in matrix_sizes:
        execution_time = matrix_multiply(n)
        execution_times.append(execution_time)
        print(f"Execution time for n = {n} is {execution_time} seconds")
    # Plot the execution times as a function of matrix size (you can use libraries like matplotlib)

    plt.plot(matrix_sizes, execution_times)
    plt.title('Matrix Multiplication Execution Time')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Execution Time (s)')
    plt.savefig('/app/plot.png')
    # plt.show()
