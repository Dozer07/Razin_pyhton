
import sqlite3
import os
import re

# Название файла базы данных
DB_NAME = 'credit_database.db'

def create_table(conn):
    """Создает таблицу 'Клиент', если она не существует."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Клиент (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ФИО_клиента TEXT NOT NULL,
                ФИО_сотрудника TEXT NOT NULL,
                срок_кредита INTEGER NOT NULL,
                процент_кредита REAL NOT NULL,
                сумма_кредита REAL NOT NULL
            )
        """)
        conn.commit()
        print("Таблица 'Клиент' успешно создана (или уже существовала).")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")

def validate_data(fio_client, fio_employee, term, rate, amount):
    """Валидирует введенные данные."""
    if not re.match(r'^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$', fio_client):
        raise ValueError("Некорректный формат ФИО клиента. Пример: Иванов Иван Иванович")
    if not re.match(r'^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$', fio_employee):
        raise ValueError("Некорректный формат ФИО сотрудника. Пример: Петров Петр Петрович")
    if not isinstance(term, int) or term <= 0:
        raise ValueError("Срок кредита должен быть целым положительным числом.")
    if not isinstance(rate, float) or rate <= 0:
        raise ValueError("Процент кредита должен быть положительным числом.")
    if not isinstance(amount, float) or amount <= 0:
        raise ValueError("Сумма кредита должна быть положительным числом.")
    return True


def insert_data(conn, fio_client, fio_employee, term, rate, amount):
    """Вставляет данные о клиенте в таблицу 'Клиент'."""
    try:
        if validate_data(fio_client, fio_employee, term, rate, amount):
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Клиент (ФИО_клиента, ФИО_сотрудника, срок_кредита, процент_кредита, сумма_кредита)
                VALUES (?, ?, ?, ?, ?)
            """, (fio_client, fio_employee, term, rate, amount))
            conn.commit()
            print("Данные успешно добавлены.")
    except sqlite3.Error as e:
        print(f"Ошибка при вставке данных: {e}")
    except ValueError as ve:
        print(f"Ошибка валидации данных: {ve}")

def search_data(conn, search_field, search_value):
    """Осуществляет поиск данных в таблице 'Клиент' по заданному полю и значению.
    Предоставляет три разных SQL-запроса для поиска.
    """
    try:
        cursor = conn.cursor()

        # Запрос 1: Поиск по точному соответствию значения
        if search_field == "ФИО_клиента" or search_field == "ФИО_сотрудника":
            query1 = f"SELECT * FROM Клиент WHERE {search_field} = ?"
            cursor.execute(query1, (search_value,))
        elif search_field == "срок_кредита":
            query1 = f"SELECT * FROM Клиент WHERE {search_field} = ?"
            cursor.execute(query1, (int(search_value),))
        else:
            query1 = f"SELECT * FROM Клиент WHERE {search_field} = ?"
            cursor.execute(query1, (float(search_value),))

        results1 = cursor.fetchall()
        print("\nРезультаты поиска (Точное соответствие):")
        for row in results1: print(row)


        # Запрос 2: Поиск по частичному соответствию (LIKE) для текстовых полей
        if search_field == "ФИО_клиента" or search_field == "ФИО_сотрудника":
            query2 = f"SELECT * FROM Клиент WHERE {search_field} LIKE ?"
            cursor.execute(query2, (f"%{search_value}%",))
            results2 = cursor.fetchall()
            print("\nРезультаты поиска (Частичное соответствие):")
            for row in results2: print(row)
        else:
            print("\nЧастичный поиск применим только к текстовым полям (ФИО).")
            results2 = [] #Пустой список, чтобы избежать ошибок в дальнейшем


        # Запрос 3: Поиск с использованием диапазонов (для числовых полей)
        if search_field == "срок_кредита" or search_field == "процент_кредита" or search_field == "сумма_кредита":
            min_value = input(f"Введите минимальное значение для {search_field}: ")
            max_value = input(f"Введите максимальное значение для {search_field}: ")
            try:
                min_value = float(min_value)
                max_value = float(max_value)
                query3 = f"SELECT * FROM Клиент WHERE {search_field} BETWEEN ? AND ?"
                cursor.execute(query3, (min_value, max_value))
                results3 = cursor.fetchall()
                print("\nРезультаты поиска (Диапазон):")
                for row in results3: print(row)
            except ValueError:
                print("Ошибка: Некорректный ввод числовых значений для диапазона.")
                results3 = []
        else:
            print("\nДиапазонный поиск применим только к числовым полям.")
            results3 = [] # Пустой список чтобы избежать ошибок в дальнейшем

        if not results1 and not results2 and not results3:
            print("Ничего не найдено.")


    except sqlite3.Error as e:
        print(f"Ошибка при поиске данных: {e}")

def delete_data(conn, delete_field, delete_value):
    """Удаляет данные из таблицы 'Клиент' по заданному полю и значению.
       Предоставляет три различных SQL-запроса для удаления.
    """
    try:
        cursor = conn.cursor()

        # Запрос 1: Удаление по точному соответствию (DELETE WHERE =)
        query1 = f"DELETE FROM Клиент WHERE {delete_field} = ?"
        cursor.execute(query1, (delete_value,))
        conn.commit()
        print(f"Удалено {cursor.rowcount} записей (Точное соответствие).")



        # Запрос 2: Удаление по частичному соответствию (DELETE WHERE LIKE) для текстовых полей
        if delete_field == "ФИО_клиента" or delete_field == "ФИО_сотрудника":
            query2 = f"DELETE FROM Клиент WHERE {delete_field} LIKE ?"
            cursor.execute(query2, (f"%{delete_value}%",))
            conn.commit()
            print(f"Удалено {cursor.rowcount} записей (Частичное соответствие).")
        else:
            print("Частичное удаление применимо только к текстовым полям (ФИО).")

        # Запрос 3: Удаление с использованием операторов сравнения (DELETE WHERE > или <) для числовых полей
        if delete_field == "срок_кредита" or delete_field == "процент_кредита" or delete_field == "сумма_кредита":
            comparison_operator = input("Введите оператор сравнения (> или <): ")
            if comparison_operator in (">", "<"):
                try:
                    delete_value = float(delete_value)
                    query3 = f"DELETE FROM Клиент WHERE {delete_field} {comparison_operator} ?"
                    cursor.execute(query3, (delete_value,))
                    conn.commit()
                    print(f"Удалено {cursor.rowcount} записей (Сравнение {comparison_operator}).")
                except ValueError:
                    print("Ошибка: Некорректный ввод числового значения.")
            else:
                print("Ошибка: Некорректный оператор сравнения.")
        else:
            print("Удаление с операторами сравнения применимо только к числовым полям.")

    except sqlite3.Error as e:
        print(f"Ошибка при удалении данных: {e}")

def update_data(conn, record_id, update_field, update_value):
    """Обновляет данные в таблице 'Клиент' для записи с заданным ID.
        Предоставляет три разных SQL-запроса для обновления.
    """
    try:
        cursor = conn.cursor()
        record_id = int(record_id) # Convert record_id to integer for security.

        # Запрос 1: Обновление одного поля (UPDATE SET поле = значение WHERE id = id)
        query1 = f"UPDATE Клиент SET {update_field} = ? WHERE id = ?"
        if update_field == "срок_кредита":
            cursor.execute(query1, (int(update_value), record_id))
        elif update_field == "процент_кредита" or update_field == "сумма_кредита":
            cursor.execute(query1, (float(update_value), record_id))
        else:
            cursor.execute(query1, (update_value, record_id))
        conn.commit()
        print(f"Обновлено {cursor.rowcount} записей (Обновление одного поля).")



        # Запрос 2: Обновление нескольких полей (UPDATE SET поле1 = значение1, поле2 = значение2 WHERE id = id) - Фиксированные поля для примера
        if update_field != "ФИО_клиента": #Чтобы не повторяться с update_field
            new_fio = input("Введите новое ФИО клиента (или оставьте пустым, чтобы не менять): ")
            if new_fio:
                query2 = "UPDATE Клиент SET ФИО_клиента = ? WHERE id = ?"
                cursor.execute(query2, (new_fio, record_id))
                conn.commit()
                print(f"Обновлено {cursor.rowcount} записей (Обновление ФИО клиента).")
        else:
           print("Для демонстрации работы нескольких полей, здесь предложено обновить ФИО клиента, если это не основное поле для обновления.")




        # Запрос 3: Обновление с использованием математических операций (для числовых полей, например, увеличить сумму кредита на процент)
        if update_field == "сумма_кредита":
            try:
                increase_percent = float(input("Введите процент увеличения суммы кредита (например, 10 для 10%): "))
                query3 = f"UPDATE Клиент SET {update_field} = {update_field} * (1 + ? / 100) WHERE id = ?"
                cursor.execute(query3, (increase_percent, record_id))
                conn.commit()
                print(f"Обновлено {cursor.rowcount} записей (Увеличение суммы кредита на {increase_percent}%).")
            except ValueError:
                print("Ошибка: Некорректный ввод процента увеличения.")
        else:
            print("Обновление с математическими операциями применимо только к полю 'сумма_кредита'.")


    except sqlite3.Error as e:
        print(f"Ошибка при обновлении данных: {e}")
    except ValueError as ve:
        print(f"Ошибка: Некорректный ввод ID записи: {ve}")


def display_menu(conn):
    """Отображает меню для работы с базой данных и обрабатывает выбор пользователя."""
    while True:
        print("\nМеню:")
        print("1. Ввести данные о клиенте")
        print("2. Поиск данных о клиенте")
        print("3. Удалить данные о клиенте")
        print("4. Редактировать данные о клиенте")
        print("5. Вывести все записи")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            fio_client = input("Введите ФИО клиента: ")
            fio_employee = input("Введите ФИО сотрудника банка: ")
            try:
                term = int(input("Введите срок кредита (в месяцах): "))
                rate = float(input("Введите процент кредита: "))
                amount = float(input("Введите сумму кредита: "))
                insert_data(conn, fio_client, fio_employee, term, rate, amount)
            except ValueError:
                print("Ошибка: Некорректный ввод числовых данных.")


        elif choice == '2':
            search_field = input("Введите поле для поиска (ФИО_клиента, ФИО_сотрудника, срок_кредита, процент_кредита, сумма_кредита): ")
            search_value = input("Введите значение для поиска: ")
            search_data(conn, search_field, search_value)

        elif choice == '3':
            delete_field = input("Введите поле для удаления (ФИО_клиента, ФИО_сотрудника, срок_кредита, процент_кредита, сумма_кредита): ")
            delete_value = input("Введите значение для удаления: ")
            delete_data(conn, delete_field, delete_value)

        elif choice == '4':
            record_id = input("Введите ID записи для редактирования: ")
            update_field = input("Введите поле для изменения (ФИО_клиента, ФИО_сотрудника, срок_кредита, процент_кредита, сумма_кредита): ")
            update_value = input("Введите новое значение: ")
            update_data(conn, record_id, update_field, update_value)

        elif choice == '5':
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Клиент")
                results = cursor.fetchall()
                print("\nВсе записи:")
                for row in results:
                    print(row)
            except sqlite3.Error as e:
                print(f"Ошибка при выводе данных: {e}")


        elif choice == '0':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    print("Выход из программы.")



if __name__ == "__main__":
    # Проверяем, существует ли файл базы данных
    db_exists = os.path.exists(DB_NAME)

    try:
        conn = sqlite3.connect(DB_NAME)
        print("Успешное подключение к базе данных.")

        # Создаем таблицу, только если база данных новая
        if not db_exists:
             create_table(conn)

        display_menu(conn) # Запускаем основное меню

    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    finally:
        if conn:
            conn.close()
            print("Соединение с базой данных закрыто.")
