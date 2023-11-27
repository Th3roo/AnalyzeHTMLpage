import requests
from bs4 import BeautifulSoup, Comment
import os

# Функция для удаления пустых строк из файла
def remove_empty_lines(filename):
  # Проверка на существование файла
  if not os.path.isfile(filename):
      print("{} does not exist".format(filename))
      return

  # Чтение всех строк из файла
  with open(filename, 'r', encoding="utf8") as filehandle:
      lines = filehandle.readlines()

  # Удаление пустых строк и запись обратно в файл
  with open(filename, 'w', encoding="utf8") as filehandle:
      lines = [line for line in lines if line.strip()]
      filehandle.writelines(lines)

# Функция для удаления дубликатов из файла
def remove_duplicates(inputFile):
   # Чтение всех строк из файла в список
   with open(inputFile, 'r', encoding='utf-8') as f:
       lines = f.readlines()

   # Удаление дубликатов с использованием словаря, сохранение порядка строк
   lines = list(dict.fromkeys(lines))

   # Запись обратно в файл
   with open(inputFile, 'w', encoding='utf-8') as f:
       f.writelines(lines)

# Список URL-ов глав конституции
urls = [
 "http://constitution.ru/10003000/10003000-3.htm",
 "http://constitution.ru/10003000/10003000-4.htm",
 "http://constitution.ru/10003000/10003000-5.htm",
 "http://constitution.ru/10003000/10003000-6.htm",
 "http://constitution.ru/10003000/10003000-7.htm",
 "http://constitution.ru/10003000/10003000-8.htm",
 "http://constitution.ru/10003000/10003000-9.htm",
 "http://constitution.ru/10003000/10003000-10.htm",
 "http://constitution.ru/10003000/10003000-11.htm"
]

# Создание файла constitution.txt, если он не существует
if not os.path.exists('constitution.txt'):
  with open('constitution.txt', 'w', encoding='utf-8') as f:
      pass

# Открытие файла для записи
with open('constitution.txt', 'w', encoding='utf-8') as f:
 # Парсинг каждой страницы
 for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(response.content.decode('cp1251'), 'html.parser')

  # Извлечение заголовков и абзацев с классом "stat"
  headers = soup.find_all(['h1', 'h2'])
  stat_paragraphs = soup.find_all('p', class_='stat')

  # Запись заголовков и абзацев в файл
  for header in headers:
    f.write(header.get_text() + '\n')
  for stat_paragraph in stat_paragraphs:
    f.write(stat_paragraph.get_text() + '\n')
    article_paragraphs = stat_paragraph.find_next_siblings('p')
    for paragraph in article_paragraphs:
      if isinstance(paragraph.next_element, Comment) and 'blockend' in paragraph.next_element:
        break
      f.write(paragraph.get_text() + '\n')
    f.write('\n') # Вставка пустой строки между статьями

# Удаление пустых строк из файла constitution.txt
remove_empty_lines('constitution.txt')

# Удаление дубликатов из файла constitution.txt
remove_duplicates('constitution.txt')

