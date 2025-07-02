#Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Найти количество слов, которые содержат ровно три буквы «А».
def count_words_with_three_a(text):

  count = 0
  words = text.split()

  for word in words:
    a_count = word.count('А')
    if a_count == 3:
      count += 1
  return count

text = "МАМА ПАПА ААА АААА АА БАРАБАН АБАКАН ТАРАКАН"
result = count_words_with_three_a(text)
print(f"Количество слов с тремя 'А': {result}")
