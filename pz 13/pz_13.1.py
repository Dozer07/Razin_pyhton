# В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.
import random

def process_2d_list():
    """
    Находит отрицательные элементы в двумерном списке, формирует новый массив
    и выводит его размер.
    """
    matrix = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]
    negative_elements = [num for row in matrix for num in row if num < 0]

    print("Исходная матрица:")
    for row in matrix: print(row)

    print("\nОтрицательные элементы:", negative_elements)
    print("Размер массива:", len(negative_elements))

if __name__ == "__main__":
    process_2d_list()

