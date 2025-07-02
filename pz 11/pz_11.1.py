# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Элементы кратные 3:
# Произведение элементов:
# Минимальный элемент:
# Содержимое второго файла:
# Элементы кратные 5:
# Количество элементов:
# Среднее арифметическое элементов:

import random
import string

def process_numbers():
    """Генерирует числа, вычисляет параметры и записывает в файл."""
    nums1 = [random.randint(-100, 100) for _ in range(20)]
    nums2 = [random.randint(-100, 100) for _ in range(20)]

    mult3 = [n for n in nums1 if n % 3 == 0]
    prod = 1
    for n in mult3: prod *= n
    min_num = min(nums1) if nums1 else "Пусто"

    mult5 = [n for n in nums2 if n % 5 == 0]
    avg = sum(nums2) / len(nums2) if nums2 else 0

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"Кратные 3: {mult3}\nПроизведение: {prod}\nМинимум: {min_num}\n")
        f.write(f"Кратные 5: {mult5}\nСреднее: {avg}\n")

def process_text(input_file="text18-24.txt", output_file="poem.txt"):
    """Читает текст, преобразует и записывает в файл."""
    try:
        with open(input_file, "r", encoding="utf-8") as f: text = f.read()
    except FileNotFoundError: return print(f"Файл {input_file} не найден")
    except IOError as e: return print(f"Ошибка чтения: {e}")

    letter_count = sum(1 for char in text if char.isalpha())
    # Исправлено:  Разбиваем текст на строки, а затем объединяем их
    words = text.upper().split()
    poem_lines = []
    for i in range(0, len(words), 30):
        poem_lines.append(" ".join(words[i:i+30])) # Join the words in each line to create string
    poem = "\n".join(poem_lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Букв: {letter_count}\n\n{poem}")

def main():
    process_numbers()
    process_text()

if __name__ == "__main__":
    main()

