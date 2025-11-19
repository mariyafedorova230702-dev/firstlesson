# Создайте множество с числами: {5, 2, 8, 2, 5, 1, 9, 2}
# 1. Выведите множество (дубликаты должны исчезнуть)
# 2. Выведите количество элементов в множестве
# 3. Проверьте, есть ли число 5 в множестве (используйте in)
# 4. Проверьте, есть ли число 100 в множестве

# set_numders = {5, 2, 8, 2, 5, 1, 9, 2}
# print(set_numders)
# print(len(set(set_numders)))
# print('есть ли 5? ',5 in set_numders)
# print('есть ли 100? ',100 in set_numders)



# Создайте два множества:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# 1. Найдите пересечение (общие элементы)
# 2. Найдите объединение (все элементы)
# 3. Найдите разность (что только в set1)
# 4. Выведите все результаты

# set_number1 = {1, 2, 3, 4, 5}
# set_number2 = {4, 5, 6, 7, 8}
# result = set_number1.intersection(set_number2)
# print(result)
# result2 = set_number1.union(set_number2)
# print(result2)
# result3 = set_number1.difference(set_number2)
# print(result3)



# Создайте список: ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'date']
# 1. Преобразуйте список в множество (используйте set())
# 2. Выведите множество (без дубликатов)
# 3. Выведите количество уникальных элементов
# 4. Преобразуйте множество обратно в список (используйте list())

# fruts = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'date']
# set_fruts = set(fruts)
# print(set_fruts)
# print(len(set(set_fruts)))
# set_fruts = list(set_fruts)
# print(set_fruts)



# Создайте словарь студента:
# {
#     'name': 'Александр',
#     'age': 20,
#     'city': 'Алматы',
#     'grade': 95
# }
#
# 1. Выведите весь словарь
# 2. Выведите значение ключа 'name'
# 3. Выведите значение ключа 'age'
# 4. Добавьте новый ключ 'email' со значением 'alex@mail.com'
# 5. Выведите обновленный словарь

# student = {
#     'name': 'Александр',
#     'age': 20,
#     'city': 'Алматы',
#     'grade': 95
# }
# print(student)
# print(student['name'])
# print(student['age'])
# student['email'] = "alex@mail.com"
# print(student)

# Создайте словарь: {'name': 'Мария', 'age': 25, 'city': 'Астана', 'job': 'Teacher'}
# 1. Измените возраст на 26
# 2. Измените город на 'Кокшетау'
# 3. Удалите ключ 'job' (используйте pop)
# 4. Выведите словарь после каждого изменения

# user = {'name': 'Мария', 'age': 25, 'city': 'Астана', 'job': 'Teacher'}
# user.update({'age': '26'})
# print(user)
# user.update({'city':'Кокшетау'})
# print(user)
# user.pop('job')
# print(user)



# Создайте словарь: {'Python': 8, 'Java': 7, 'C++': 6, 'JavaScript': 9}
# (язык программирования: популярность)
#
# 1. Используя цикл for, выведите все ключи
# 2. Используя цикл for, выведите все значения
# 3. Используя цикл for, выведите ключи и значения
#    Формат: "Python - популярность 8"
# 4. Выведите только языки с популярностью >= 8

# languages = {'Python': 8, 'Java': 7, 'C++': 6, 'JavaScript': 9}
# for language in languages:
#     print('ключи ',language)
# for language in languages:
#     print('значения',languages[language])
# for language, popular in languages.items():
#     print(f'{language} - популярность {popular}')
# print('самые популярные:')
# for language,popular in languages.items():
#     if popular >= 8:
#         print(f'{language} - популярность {popular}') 

# Попросите пользователя ввести 5 чисел
# Используя цикл while, добавьте все числа в множество
# Выведите множество (без дубликатов)
# Выведите количество уникальных чисел
# uniq_num = set()
# count = 0
# while count < 5 :
#     num = int(input('enter 5 numbers:'))
#     uniq_num.add(num)
#     count+=1
# print(uniq_num)
# print(len(uniq_num))    



# # Создайте словарь с оценками студентов:
# # students = {
# #     'Алиса': 85,
# #     'Боб': 92,
# #     'Виктор': 78,
# #     'Галина': 95,
# #     'Дмитрий': 88
# # }
# #
# # Используя цикл for:
# # 1. Выведите каждого студента и его оценку
# # 2. Подсчитайте среднюю оценку (sum / len)
# # 3. Найдите студента с максимальной оценкой
# # 4. Найдите студента с минимальной оценкой

# students = {
#     'Алиса': 85,
#     'Боб': 92,
#     'Виктор': 78,
#     'Галина': 95,
#     'Дмитрий': 88
# }

# for student,grade in students.items():
#     print(student, '-', grade)

# summ = 0
# for grade in students.values():
#     summ+=grade
# average = summ/len(students)
# print(average)    


# Создайте список слов: ['cat', 'dog', 'cat', 'bird', 'dog', 'dog', 'cat', 'fish']
#
# 1. Используйте словарь для подсчета каждого слова
#    Результат: {'cat': 3, 'dog': 3, 'bird': 1, 'fish': 1}
# 2. Используя цикл for, вывести каждое слово и его количество
#    Формат: "cat встречается 3 раз"
# 3. Используйте множество для поиска уникальных слов
# 4. Выведите количество уникальных слов

# animals = ['cat', 'dog', 'cat', 'bird', 'dog', 'dog', 'cat', 'fish']
# animal_count = {}

# for animal in animals:
#     if animal in animal_count:
#         animal_count[animal] += 1
#     else:
#         animal_count[animal]= 1

# print(animal_count)
# for animal, count in animal_count.items():
#     print(f'{animal} встречается - {count}')

# uniq_animal = set(animals)
# print(uniq_animal)

# print('Количество уникальных: ', len(uniq_animal))


# Создайте словарь с хобби студентов:
# hobbies = {
#     'Алиса': ['рисование', 'музыка', 'спорт'],
#     'Боб': ['программирование', 'игры', 'спорт'],
#     'Виктор': ['музыка', 'кино', 'спорт'],
#     'Галина': ['рисование', 'книги', 'путешествия']
# }
#
# Используя цикл for:
# 1. Выведите каждого студента и его хобби
#    Формат: "Алиса: рисование, музыка, спорт"
# 2. Найдите все уникальные хобби (используйте set)
# 3. Выведите количество студентов, которые занимаются спортом
# 4. Выведите студента с наибольшим количеством хобби

# hobbies = {
#     'Алиса': ['рисование', 'музыка', 'спорт'],
#     'Боб': ['программирование', 'игры', 'спорт'],
#     'Виктор': ['музыка', 'кино', 'спорт'],
#     'Галина': ['рисование', 'книги', 'путешествия']
# }

# for sudent, hobs in hobbies.items():
#     print(f"{sudent}: {', '.join(hobs)}")

# uniq_hobbi = set()
# for hobs in hobbies.values():
#     for hob in hobs:
#         uniq_hobbi.update(hob)
# print('Уникальные хобби: ', uniq_hobbi)        
# print(len(uniq_hobbi))

# sport_count = 0
