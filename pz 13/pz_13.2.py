# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
import random

def average_odd_rows():
    """
    Для каждой строки матрицы с нечетным номером находит среднее арифметическое ее элементов.
    """
    matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

    print("Исходная матрица:")
    for row in matrix: print(row)

    for i in range(len(matrix)):
        if (i + 1) % 2 != 0:
            avg = sum(matrix[i]) / len(matrix[i])
            print(f"Среднее строки {i + 1}: {avg}")

if __name__ == "__main__":
    average_odd_rows()
