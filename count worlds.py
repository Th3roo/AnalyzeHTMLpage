import re
import os
def create_patterns(surname):
   """Создает регулярные выражения для каждой буквы в фамилии."""
   return [f"^{surname[i]}.*" for i in range(len(surname))]

def find_matches(patterns, text):
   """Ищет все слова, соответствующие каждому регулярному выражению."""
   return [re.findall(pattern, text) for pattern in patterns]

def count_matches(matches):
   """Подсчитывает количество совпадений для каждого регулярного выражения."""
   return [len(match) for match in matches]

def write_counts(counts, filename):
  """Записывает результаты в файл. Если файл или папка не существуют, они создаются."""
  directory = os.path.dirname(filename)
  if not os.path.exists(directory):
      os.makedirs(directory)
  if not os.path.exists(filename):
      open(filename, 'w').close()
  try:
      with open(filename, 'w') as f:
          for count in counts:
              f.write(str(count) + '\n')
  except IOError as e:
      print(f"Ошибка при записи в файл: {e}")

def read_file(filename):
   """Читает весь текст из файла и возвращает его."""
   with open(filename, 'r', encoding='utf-8') as file:
       text = file.read()
   return text


# Ваша фамилия
surname = "Айдаров"

# Текст, в котором нужно искать слова
text = read_file("constitution.txt")

# Создаем регулярные выражения
patterns = create_patterns(surname)

# Ищем все слова, соответствующие каждому регулярному выражению
matches = find_matches(patterns, text)

# Получаем количество совпадений
counts = count_matches(matches)

# Сохраняем результаты в файл
write_counts(counts, 'public_html/constitution.html')

print(text)
print(counts)
print(patterns)

