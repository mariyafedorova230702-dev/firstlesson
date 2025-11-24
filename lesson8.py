# 1. Создайте файл 'text.txt' с несколькими строками в РАЗНОМ регистре
#    Пример: "Привет МИР", "PyThOn", "файлы И ДАННЫЕ"
# 2. Откройте файл и прочитайте содержимое
# 3. Переведите весь текст в ВЕРХНИЙ регистр (используйте .upper())
# 4. Сохраните результат в новый файл 'text_upper.txt'
# 5. Откройте оба файла и выведите их содержимое
# Покажите исходный файл и результат


# with open ('text.txt', 'w', encoding='utf-8') as file:
#     file.write("Привет МИР\n")
#     file.write("PyThOn\n")
#     file.write("файлы И ДАННЫЕ\n")
# with open ('text.txt', 'r', encoding='utf-8') as file:
#     text = file.read() 


# text_upper = text.upper()
# with open('text_upper.txt','w', encoding='utf-8') as file:
#     file.write(text_upper)

# with open('text.txt','r',encoding='utf-8') as file:
#     print(file.read())   

# with open('text_upper.txt', 'r', encoding='utf-8') as file:
#     print(file.read())


# 1. Создайте два файла:
#    - 'file1.txt' с текстом: "Первый файл"
#    - 'file2.txt' с текстом: "Второй файл"
# 2. Прочитайте содержимое обоих файлов
# 3. Объедините содержимое в одну переменную (с разделением)
# 4. Запишите объединенный текст в новый файл 'merged.txt'
# 5. Выведите содержимое объединенного файла
# Формат: "Первый файл\n---\nВторой файл"

# with open('file1.txt','w', encoding='utf-8') as file:
#     file.write("Первый файл")
   
# with open ('file2.txt', 'w', encoding='utf-8') as file:
#     file.write("Второй файл")  

# with open('file1.txt','r',encoding='utf-8') as file:
#     text1 = file.read()
#     print(text1)

# with open('file2.txt', 'r', encoding='utf-8') as file:
#     text2 = file.read()
#     print(text2)

# merged_text = text1 + "\n---\n"+ text2

# with open('merged_text.txt','w', encoding='utf-8') as file:
#     file.write(merged_text)
# with open ('merged_text.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

# 1. Создайте файл 'words.txt' с текстом:
#    "cat dog cat bird dog dog cat fish bird cat"
# 2. Прочитайте файл и разделите на слова (используйте .split())
# 3. Используя словарь, подсчитайте сколько раз встречается каждое слово
# 4. Сохраните результаты в файл 'word_count.txt' в формате:
#    "слово: количество" (каждое на новой строке)
# 5. Выведите оригинальный файл и файл со статистикой

# with open('words.txt', 'w', encoding='utf-8') as file:
#     file.write("cat dog cat bird dog dog cat fish bird cat")

# with open('words.txt', 'r', encoding='utf-8') as file :
#     text = file.read()    

# words = text.split()

# word_count = {}

# for w in words:
#     if w in word_count:
#         word_count[w] += 1
#     else:
#         word_count[w] = 1   

# with open('word_count.txt','w',encoding='utf-8') as file:
#     for word,count in word_count.items():
#         file.write(f"{word}:{count}\n")    
             
# print('word.txt: ')
# with open('words.txt','r', encoding='utf-8') as file:
#     print(file.read())



# 1. Создайте файл 'ages.txt' с возрастом людей (каждый на новой строке):
#    10, 15, 20, 25, 30, 35, 40, 45, 50
# 2. Прочитайте файл
# 3. Найдите все возрасты от 25 до 40 (включительно)
# 4. Запишите найденные возрасты в новый файл 'filtered_ages.txt'
# 5. Выведите оба файла на консоль


# with open('ages.txt', 'w',encoding='utf-8') as file:
#     file.write("10\n15\n20\n25\n30\n35\n40\n45\n50")
# with open('ages.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     lines = content.strip().split('\n')
       
# ages = []
# for line in lines:
#     number = int(line)
#     ages.append(number)
# filtered = []
# for number in ages:
#    if 25 <= number <= 40: 
#        filtered.append(number)

# with open('filtered_ages.txt', 'w', encoding='utf-8') as file:
#     for number in filtered:
#         file.write(str(number) + '\n')
# print('ages.txt')
# with open('ages.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

# print('filtered_ages.txt: ')  
# with open('filtered_ages.txt', 'r', encoding='utf-8') as file:
#     print(file.read())     
             


# 1. Создайте файл 'products.txt' с товарами в формате:
#    "Название: Цена" (каждый товар на новой строке)
#    Пример:
#    Яблоки: 150
#    Бананы: 200
#    Апельсины: 180
#    Груши: 220
#
# 2. Прочитайте файл и обработайте данные
# 3. Создайте словарь товаров {название: цена}
# 4. Найдите товар с максимальной ценой
# 5. Найдите товар с минимальной ценой
# 6. Вычислите среднюю цену всех товаров
# 7. Выведите результаты на консоль


# with open('products.txt','w', encoding='utf-8') as file:
#     file.write("Яблоки: 150\n")
#     file.write("Бананы: 200\n")
#     file.write("Апельсины: 180\n")
#     file.write("Груши: 220\n")
# with open('products.txt', 'r', encoding='utf-8') as file:
#     lines = file.read().strip().split("\n")

# products = {}
# for line in lines :
#     name, price = line.split(":")
#     name = name.strip()
#     price = int(price.strip())
#     products[name] = price

# max_product  = None
# max_price = -1

# for price in products.values():
#     if price > max_price:
#         max_price = price
#         max_product = name

# total =0
# count = 1
# for price in products.values():
#     total += price
#     count = 1
 
# average_price = total / count

# print('Словарь товаров: ', products)
# print('Самый дорогой товар:', max_product, "-", max_price)
# print("Средняя цена: ", average_price)

# 1. Создайте файл 'messy_data.txt' с текстом в разном регистре:
#    "PYTHON Programming", "JavaScript", "SQL", "CSS"
# 2. Прочитайте файл
# 3. Переведите каждую строку в нижний регистр (.lower())
# 4. Удалите пробелы в начале и конце каждой строки (.strip())
# 5. Сохраните очищенные данные в файл 'clean_data.txt'
# 6. Выведите исходный и очищенный файл рядом

# with open('messy_data.txt', 'w', encoding='utf-8') as file:
#     file.write("PYTHON Programming\n")
#     file.write("JavaScrip\n")
#     file.write("SQL\n")
#     file.write("CSS\n")
# with open ('messy_data.txt', 'r', encoding='utf-8') as file:
#     lines = file.read()

# clean_lines = [] 
# for  line in lines:
#     clean_line =  line.strip().lower()
#     clean_lines.append(clean_line)

# with open ('clean_data.txt', 'w',encoding='utf-8') as file:
#     for line in clean_lines:
#         file.write(line +"\n")


# print('meessy_data.txt: ')
# with open ('clean_data.txt', 'r',encoding='utf-8') as file :
#         print(file.read())

# print('clean_data.txt: ') 
# with open('clean_data.txt','r', encoding='utf-8') as file:
#          print(file.read())


# 1. Создайте файл 'article.txt' с несколькими строками текста
# 2. Прочитайте файл
# 3. Подсчитайте:
#    - Количество строк
#    - Количество слов (используйте .split())
#    - Количество символов (используйте len())
#    - Количество символов без пробелов
# 4. Выведите все результаты на консоль
# Формат вывода:
# "Строк: X, Слов: X, Символов: X, Символов без пробелов: X"

# with open('article.txt','w',encoding='utf-8') as file:
#     file.write('ahah ahah ahaha hah ahah')
#     file.write('agga ga gagaga gaga gaga ga')
#     file.write('fafafafaff afaaf fafafaf affafa')

# with open('article.txt', 'r',encoding='utf-8') as file:
#         lines = file.readlines()

# num_lines =len(lines)

# num_words = 0
# num_chars = 0
# num_chars_no_spaces = 0

# for line in lines :
#     words_in_line = line.split()
#     num_words += len(words_in_line)
#     num_chars += len(line)
#     num_chars_no_spaces += len(line.replace(" ",""))

# print(f"Строк: {num_lines}, Слов: {num_words}, Символов: {num_chars}, Символов без проблов: {num_chars_no_spaces}")




# 1. Создайте файл 'numbers.txt' с числами (некоторые повторяются):
#    1, 2, 3, 2, 4, 5, 1, 3, 6, 2
# 2. Прочитайте файл и разделите числа
# 3. Используя set(), найдите только УНИКАЛЬНЫЕ числа
# 4. Запишите уникальные числа в файл 'unique_numbers.txt'
# 5. Выведите оригинальный файл, количество всех чисел и количество уникальных

with open('numbers.txt','w',encoding='utf-8') as file:
    file.write("1, 2, 3, 2, 4, 5, 1, 3, 6, 2")

with open('numbers.txt', 'r',encoding='utf-8') as file:
    content = file.read()

numbers = content.split()
numbers = [int (num.strip())]