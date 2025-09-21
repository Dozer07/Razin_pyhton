class Computer:
    """
    Класс, представляющий компьютер.
    """

    def __init__(self, mark, processor, ram):
        """
        Инициализирует объект компьютера.

        Args:
            mark (str): Марка компьютера.
            processor (str): Тип процессора.
            ram (int): Объем оперативной памяти (в ГБ).
        """
        self.mark = mark
        self.processor = processor
        self.ram = ram

    def display_info(self):
        """
        Выводит информацию о компьютере в заданном формате.
        """
        return f"Марка: {self.mark}, Процессор: {self.processor}, Оперативная память: {self.ram} ГБ"


# Тестовые запуски (создание объектов и вывод информации)
if __name__ == "__main__":
    computer1 = Computer("Dell", "Intel Core i5", 8)
    computer2 = Computer("Apple", "M1", 16)
    computer3 = Computer("HP", "AMD Ryzen 7", 32)

    print(computer1.display_info())
    print(computer2.display_info())
    print(computer3.display_info())
