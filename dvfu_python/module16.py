# task A
import math

x = float(input())

result = math.log(x ** (3 / 16), 32) + x ** math.cos((x * math.pi) / (2 * math.e)) - math.sin(x / math.pi) ** 2

print(result)

# task B
import sys
from math import gcd
from functools import reduce


def compute_gcd_of_sequence(sequence):
    return reduce(gcd, sequence)


input_lines = sys.stdin.read().strip().splitlines()

results = []
for line in input_lines:
    numbers = list(map(int, line.split()))
    result = compute_gcd_of_sequence(numbers)
    results.append(result)

for res in results:
    print(res)

# task C
from math import comb

n, m = map(int, input().split())

total_combinations = comb(n, m)

successful_combinations = comb(n - 1, m - 1)

print(successful_combinations, total_combinations)

# task D
import math
import sys

input_data = sys.stdin.read().strip()
numbers = list(map(float, input_data.split()))

product = 1
n = len(numbers)
for number in numbers:
    product *= number

geometric_mean = product ** (1 / n)

print(geometric_mean)

# task E
import math


x, y = map(float, input().split())

rho, phi = map(float, input().split())

x_p = rho * math.cos(phi)
y_p = rho * math.sin(phi)

distance = math.sqrt((x - x_p)**2 + (y - y_p)**2)

print(distance)

# task F
import numpy as np


def multiplication_matrix(n):
    return np.array([[(i + 1) * (j + 1) for j in range(n)] for i in range(n)])

# task G
import numpy as np


def make_board(size):
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board

# task H
import numpy as np


def make_board(size):
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


def snake(M, N, direction='H'):

    if direction == 'H':
        matrix = np.arange(1, M * N + 1, dtype=np.int16).reshape(N, M)
        matrix[1::2] = matrix[1::2, ::-1]
    elif direction == 'V':
        matrix = np.arange(1, M * N + 1, dtype=np.int16).reshape(M, N).T
        matrix[:, 1::2] = matrix[::-1, 1::2]
    return matrix


# task I
import numpy as np


def make_board(size):
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


def snake(M, N, direction='H'):
    if direction == 'H':
        matrix = np.arange(1, M * N + 1, dtype=np.int16).reshape(N, M)
        matrix[1::2] = matrix[1::2, ::-1]
    elif direction == 'V':
        matrix = np.arange(1, M * N + 1, dtype=np.int16).reshape(M, N).T
        matrix[:, 1::2] = matrix[::-1, 1::2]
    return matrix


def rotate(matrix, angle):
    if angle == 90:
        return np.rot90(matrix, k=-1)
    elif angle == 180:
        return np.rot90(matrix, k=2)
    elif angle == 270:
        return np.rot90(matrix, k=1)
    elif angle == 360:
        return matrix.copy()
    else:
        raise ValueError("Угол должен быть одним из значений: 90, 180, 270, 360.")

# task J
import numpy as np


def make_board(size):
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


def snake(M, N, direction='H'):
    if direction == 'H':
        matrix = np.arange(1, M * N + 1, dtype=np.int16).reshape(N, M)
        matrix[1::2] = matrix[1::2, ::-1]
    elif direction == 'V':
        matrix = np.arange(1, M * N + 1, dtype=np.int16).reshape(M, N).T
        matrix[:, 1::2] = matrix[::-1, 1::2]
    return matrix


def rotate(matrix, angle):
    if angle == 90:
        return np.rot90(matrix, k=-1)
    elif angle == 180:
        return np.rot90(matrix, k=2)
    elif angle == 270:
        return np.rot90(matrix, k=1)
    elif angle == 360:
        return matrix.copy()
    else:
        raise ValueError("Угол должен быть одним из значений: 90, 180, 270, 360.")


def stairs(vector):
    size = len(vector)
    matrix = np.zeros((size, size), dtype=vector.dtype)
    for i in range(size):
        matrix[i] = np.roll(vector, i)
    return matrix



