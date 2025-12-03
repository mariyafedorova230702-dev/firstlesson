# import random
# def sort_result(func):
#     def wrapper():


# 1. Создайте декоратор add_prefix(func)
# 2. Декоратор должен добавить "★ " перед результатом функции
# 3. Примените декоратор к функции greeting(name)
# 4. Функция greeting возвращает "Привет, {name}!"
#
# Пример:
# @add_prefix
# def greeting(name):
#     return f"Привет, {name}!"
#
# greeting('Алиса') → "★ Привет, Алиса!"
# greeting('Боб') → "★ Привет, Боб!



# def add_prefix(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         return f'[{result}]'
#     return wrapper 

# @add_prefix
# def greeting(name):
#     return f"Привет, {name}!"
# print('алиса')
# print('боб')
