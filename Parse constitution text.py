import requests
from bs4 import BeautifulSoup
import os

def remove_substring_from_file(file_path, substring):
   # Откройте файл для чтения и создайте новый файл для записи
   with open(file_path, 'r', encoding="utf8") as read_file, open('temp.txt', 'w', encoding="utf8") as write_file:
       # Прочитайте файл построчно
       for line in read_file:
           # Удалите все вхождения подстроки
           new_line = line.replace(substring, '')
           # Запишите обновленные строки в новый файл
           write_file.write(new_line)
   # Замените исходный файл новым файлом
   os.remove(file_path)
   os.rename('temp.txt', file_path)


def remove_empty_lines(filename):
   if not os.path.isfile(filename):
       print("{} does not exist".format(filename))
       return

   with open(filename, 'r', encoding="utf8") as filehandle:
       lines = filehandle.readlines()

   with open(filename, 'w', encoding="utf8") as filehandle:
       lines = [line for line in lines if line.strip()]
       filehandle.writelines(lines)

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


if not os.path.exists('constitution.txt'):
   with open('constitution.txt', 'w', encoding='utf-8') as f:
       pass # Файл будет создан, если он не существует

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
     article_text = stat_paragraph.find_next_sibling('p').get_text()
     f.write(article_text + '\n')   

remove_empty_lines('constitution.txt')
remove_substring_from_file('constitution.txt', '1.')

    
