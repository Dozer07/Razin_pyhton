#Даны координаты поля шахматной доски х, у (целые числа, лежащие в диапазоне 1-8).
# Учитывая, что левое нижнее поле доски (1,1) является черным, проверить
# истинность высказывания: «Данное поле является белым».

def is_white(x, y):
    try:
        if not (1 <= x <= 8 and 1 <= y <= 8):
            raise ValueError("Координаты должны быть в диапазоне от 1 до 8.")
        return (x + y) % 2 == 0
    except ValueError as e:
        return f"Ошибка: {e}"

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

result = is_white(x, y)
if isinstance(result, bool):
    print("Высказывание истинно" if result else "Высказывание ложно")
else:
    print(result)

