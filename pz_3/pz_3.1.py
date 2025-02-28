# Дано четырехзначное число
# Проверить истинность высказывания: «Данное число читается одинаково слева направо и справа налево».
def is_palindrome(n):
    s = str(n)
    if len(s) != 4 or not s.isdigit():
        return "Ошибка: Введено некорректное четырехзначное число."
    return s == s[::-1]

number_str = input("Введите четырехзначное число: ")
try:
    number = int(number_str)
    result = is_palindrome(number)
    print("Высказывание истинно" if result else "Высказывание ложно")
except ValueError:
    print("Ошибка: Введенное значение не является целым числом.")
