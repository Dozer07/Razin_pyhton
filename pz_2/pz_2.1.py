#Вариант 24 Найти количество полных минут, прошедших с начала суток.

try:
    N = int(input("Введите количество секунд: "))
    full_minutes = N // 60
    print("Количество полных минут:", full_minutes)
except ValueError:
    print("Ошибка: Пожалуйста, введите целое число.")


