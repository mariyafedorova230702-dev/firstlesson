# 1. Напишите функцию multiply(a, b)
# 2. Функция должна возвращать произведение двух чисел
# 3. Вызовите функцию с разными числами
#
# Пример:
# multiply(3, 4) → 12
# multiply(5, 6) → 30
# multiply(2, 9) → 18

# def muitiplay(a,b):
#     return a * b 
# print(muitiplay(3,4))
# print(muitiplay(5,6))
# print(muitiplay(2,9))



# 1. Напишите функцию greet(name, greeting='Привет')
# 2. Функция должна возвращать строку "{greeting}, {name}!"
# 3. Вызовите функцию двумя способами:
#    - С одним аргументом (используется значение по умолчанию)
#    - С двумя аргументами (переданное значение)
#
# Пример:
# greet('Алиса') → "Привет, Алиса!"
# greet('Боб', 'Привет') → "Привет, Боб!"
# greet('Виктор', 'Добрый день') → "Добрый день, Виктор!"

# def greet(name, greeting='Привет'):
#     return f'{greeting}, {name}!'
# print(greet('Алиса'))
# print(greet('Боб', 'Привет'))
# print(greet('Виктор', 'Добрый день'))


# 1. Напишите функцию info(name, age=18, city='Алматы')
# 2. Функция должна возвращать строку с информацией о человеке
# 3. Вызовите функцию разными способами
#
# Пример:
# c → "Алиса, 18 лет, Алматы"
# info('Боб', 25) → "Боб, 25 лет, Алматы"
# info('Виктор', 30, 'Астана') → "Виктор, 30 лет, Астана"


# def info(name, age=18, city='Алматы'):
#     return f'{name},{age} лет, {city}'
# print(info('Алиса'))
# print(info('Боб', 25))
# print(info('Виктор', 30, 'Астана'))


# 1. Напишите функцию sum_numbers(*args)
# 2. Функция должна возвращать сумму всех переданных чисел
# 3. Используйте функцию sum() для подсчета
# 4. Вызовите функцию с разным количеством аргументов
#
# Пример:
# sum_numbers(1, 2, 3) → 6
# sum_numbers(5, 10, 15, 20) → 50
# sum_numbers(1) → 1
# sum_numbers(100, 200, 300, 400, 500) → 1500

# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 3))
# print(sum_numbers(5, 10, 15, 20))
# print(sum_numbers(1))
# print(sum_numbers(100, 200, 300, 400, 500))



# 1. Напишите функцию print_items(*args)
# 2. Функция должна вывести каждый элемент на новой строке с номером
# 3. Используйте цикл for и enumerate()
# 4. Вызовите функцию с разными элементами
#
# Пример:
# print_items('apple', 'banana', 'cherry')
# Вывод:
# 1. apple
# 2. banana
# 3. cherry

# def print_items(*args):
#     result = []
#     for i, item in enumerate(args, start=1):
#         result.append(f'{i}.{item}')
#     return '\n'.join(result)
# print(print_items('apple', 'banana', 'cherry'))




# 1. Напишите функцию count_strings(*args)
# 2. Подсчитайте сколько строк (str) в аргументах
# 3. Используйте isinstance(элемент, str) для проверки
# 4. Возвращайте количество строк
#
# Пример:
# count_strings('hello', 5, 'world', 10, 'test') → 3
# c → 0
# count_strings('a', 'b', 'c') → 3

# def count_strings(*args):
#     count = 0
#     for item in args:
#         if isinstance(item, str):
#             count += 1
#     return count     
# print(count_strings('hello', 5, 'world', 10, 'test'))
# print(count_strings('hello', 5, 'world', 10, 'test')) 
# print(count_strings('a', 'b', 'c'))  





# 1. Напишите функцию create_person(**kwargs)
# 2. Функция должна вывести информацию о человеке из словаря
# 3. Используйте цикл for и .items() для вывода
# 4. Вызовите функцию с разными параметрами
#
# Пример:
# create_person(name='Алиса', age=20, city='Алматы')
# Вывод:
# name: Алиса
# age: 20
# city: Алматы

# def create_person(**kwargs):
#     result = []
#     for key, value in kwargs.items():
#         result.append(f'{key} : {value}')
#     return '\n'.join(result)    
# print(create_person(name='Алиса', age=20, city='Алматы'))



# 1. Напишите функцию introduce(name, age, *hobbies)
# 2. name и age — обязательные параметры
# 3. hobbies — остальные аргументы (хобби)
# 4. Выведите: имя, возраст и все хобби
#
# Пример:
# introduce('Алиса', 20, 'Читать', 'Рисовать', 'Программировать')
# Вывод:
# Имя: Алиса
# Возраст: 20
# Хобби: Читать, Рисовать, Программировать

# def introduce(name, age, *hobbies):
#     result = [f"Имя: {name}", f"Возраст: {age}"]
#     if hobbies:
#         print(f"хобби: { ', '.join(hobbies)}")
#     else:
#         print('хобби: нет')
#     return '\n'.join(result)    
# print(introduce('Алиса', 20, 'Читать', 'Рисовать', 'Программировать'))            




# 1. Напишите функцию show_data(name, *numbers, **info)
# 2. name — обязательный параметр
# 3. numbers — все остальные числовые аргументы
# 4. info — все остальные именованные аргументы (словарь)
# 5. Выведите все данные структурированно
#
# Пример:
# show_data('Али', 10, 20, 30, city='Алматы', job='Engineer')
# Вывод:
# Имя: Али
# Числа: (10, 20, 30)
# Информация:
# city: Алматы
# job: Engineer

# def show_data(name, *numbers, **info):
#     result = []
#     result.append(f"Имя: {name}")
    
#     if numbers:
#         result.append(f'числа: {numbers}')
#     else:
#         result.append('числа нет')
#     if info :
#         result.append('Информация:') 
#         for key , value in info.items():
#             result.append(f'{key}:{value}')  
#     else : 
#         result.append('Информация: нет')
#     return '\n'.join(result)            
# print(show_data('Али', 10, 20, 30, city='Алматы', job='Engineer'))        





# 1. Напишите функцию apply_operation(operation, *numbers)
# 2. operation — функция, которую применять
# 3. numbers — числа, к которым применять функцию
# 4. Используйте map() для применения функции
# 5. Возвращайте список результатов
#
# Пример:
# def double(x):
#     return x * 2
#
# apply_operation(double, 1, 2, 3, 4, 5)
# → [2, 4, 6, 8, 10]
#
# def square(x):
#     return x ** 2
#
# apply_operation(square, 1, 2, 3, 4, 5)
# → [1, 4, 9, 16, 25]

# def apply_operation(operation, *numbers):
#     return(list(map(operation,numbers)))
# def square(x):
#     return x**2
# print(apply_operation(square, 1, 2, 3, 4, 5))