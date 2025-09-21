import re
import os

def find_years(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return [], 0
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return [], 0

    pattern = r'\b(1[8-9]\d{2}|20\d{2})\s(?:год(?:а|у|е|ом)?)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    count = len(matches)
    return matches, count


if __name__ == "__main__":
    filepath = "Dostoevsky.txt"
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл '{filepath}' не существует. Создайте его и добавьте контент.")
        exit()
    years, count = find_years(filepath)

    print("Найденные годы:")
    print(years)
    print("\nКоличество найденных элементов:", count)
