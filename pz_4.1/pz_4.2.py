#Даны целые положительные числа N и K. Используя только операции сложения и
#вычитания, найти частное от деления нацело N на K, а также остаток от этогоделения.
def divide_with_remainder(n, k):
    if k == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо.")
    if n < 0 or k < 0:
        raise ValueError("N и K должны быть неотрицательными.")
    частное = 0
    остаток = n

    while остаток >= k:
        остаток -= k
        частное += 1

    return частное, остаток

n = int(input("Введите N: "))
k = int(input("Введите K: "))

try:
    частное, остаток = divide_with_remainder(n, k)
    print(f"Частное: {частное}")
    print(f"Остаток: {остаток}")
except (ZeroDivisionError, ValueError) as e:
    print(f"Ошибка: {e}")



