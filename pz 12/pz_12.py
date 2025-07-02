# 1.Даны значения роста 20 юношей. Определить сколько юношей будут направлены
# в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).
# 2.Составить список, в который будут включены только согласные буквы и привести
# их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели','Каир'].
import random

def calculate_teams():
    heights = [random.randint(170, 200) for _ in range(20)]
    basketball = sum(h >= 190 for h in heights)
    print(f"Рост: {heights}\nБаскет: {basketball}, Футбол: {len(heights) - basketball}")

def consonants_to_upper():
    cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = [c.upper() for city in cities for c in city if c.isalpha() and c not in vowels]
    print(f"Согласные: {consonants}")

if __name__ == "__main__":
    calculate_teams()
    consonants_to_upper()
