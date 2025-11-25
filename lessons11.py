# 1. Напишите функцию add(a, b), которая принимает два числа
# 2. Функция должна возвращать их сумму
# 3. Вызовите функцию с разными числами и выведите результаты
#
# Пример:
# add(5, 3) → 8
# add(10, 20) → 30
# add(-5, 5) → 0


# def add(a, d):
#     return a + d
# print(add(5,3))
# print(add(10,20))
# print(add(-5,5))


# 1. Напишите функцию celsius_to_fahrenheit(celsius)
# 2. Формула: F = C * 9/5 + 32
# 3. Функция должна возвращать температуру в Фаренгейтах
# 4. Вызовите функцию для температур: 0, 25, 100, -40
#
# Пример:
# celsius_to_fahrenheit(0) → 32
# celsius_to_fahrenheit(25) → 77.0
# celsius_to_fahrenheit(100) → 212.0

# def celsius_to_fahrenheit(celsius):
#     F = celsius * 9/5 + 32
#     return F
# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(25))
# print(celsius_to_fahrenheit(100))




# 1. Напишите функцию is_even(num), которая проверяет четность
# 2. Возвращает True если число четное, False если нечетное
# 3. Вызовите функцию для чисел: 4, 7, 10, 15, 20
#
# Пример:
# is_even(4) → True
# is_even(7) → False
# is_even(10) → True

# def is_even(num):
#     return num % 2 ==0

# print(is_even(4))
# print(is_even(7))
# print(is_even(10))
# print(is_even(15))
# print(is_even(20))


# 1. Напишите функцию count_vowels(text)
# 2. Подсчитайте количество гласных букв (а, е, и, о, у, я)
# 3. Используйте цикл for для проверки каждого символа
# 4. Вызовите функцию для текстов: "hello", "Python", "яблоко"
#
# Пример:
# count_vowels("hello") → 2 (e, o)
# count_vowels("Python") → 1 (o)
# count_vowels("яблоко") → 3 (я, о, о)

# def count_vowels(text):
#     count = 0
#     for letter in text :
#         if letter in 'aeiouаеёиоуыэюя':
#             count+=1
#     return count
# print(count_vowels('hello'))
# print(count_vowels('Python'))
# print(count_vowels('яблоко'))               



# 1. Напишите функцию square(x), которая возвращает квадрат числа
# 2. Вызовите функцию для чисел: 2, 3, 5, 10
# 3. Выведите результаты
#
# Пример:
# square(2) → 4
# square(3) → 9
# square(5) → 25

# def square(x):
#     return x * x
# print(square(2))
# print(square(3))
# print(square(5))
# print(square(10))



# 1. Напишите функцию is_palindrome(text)
# 2. Проверьте является ли текст палиндромом (читается одинаково в обе стороны)
# 3. Возвращает True если палиндром, False если нет
# 4. Вызовите функцию для: "радар", "уровень", "привет", "топот"
#
# Пример:
# is_palindrome("радар") → True
# is_palindrome("уровень") → True
# is_palindrome("привет") → False
# is_palindrome("топот") → True


# def is_palindrome(text):
#     if text == text [::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome('радар'))
# print(is_palindrome('уровень'))
# print(is_palindrome('привет'))
# print(is_palindrome('топот'))


# 1. Напишите функцию max_of_two(a, b), которая возвращает большее число
# 2. Не используйте встроенную функцию max()
# 3. Используйте if/else
# 4. Вызовите функцию для пар: (5, 9), (15, 3), (10, 10)
#
# Пример:
# max_of_two(5, 9) → 9
# max_of_two(15, 3) → 15
# max_of_two(10, 10) → 10

# def max_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max_of_two(5,9))
# print(max_of_two(15,3))
# print(max_of_two(10,10))    



# 1. Напишите функцию apply_discount(price, discount_percent)
# 2. Функция должна рассчитать цену со скидкой
# 3. Возвращает новую цену
# 4. Вызовите функцию для цен: 1000, 500, 2500 со скидками 10%, 20%, 15%
#
# Пример:
# apply_discount(1000, 10) → 900 (скидка 10%)
# apply_discount(500, 20) → 400 (скидка 20%)
# apply_discount(2500, 15) → 2125 (скидка 15%)


# def apply_discount(price, discount_percent):
#     return price - (price * discount_percent / 100)
# print(apply_discount(1000,10))
# print(apply_discount(500,20))
# print(apply_discount(2500,15))




# 1. Напишите функцию multiply_three(a, b, c), которая возвращает произведение
# 2. Функция должна умножить все три числа
# 3. Вызовите функцию для разных комбинаций
#
# Пример:
# multiply_three(2, 3, 4) → 24
# multiply_three(5, 2, 3) → 30
# multiply_three(1, 1, 1) → 1

# def multiply_three(a, b, c):
#     return a * b * c
# print(multiply_three(2,3,4))
# print(multiply_three(5,2,3))
# print(multiply_three(1,1,1))




# 1. Напишите функцию get_age_category(age)
# 2. Возвращает категорию по возрасту:
#    - Если < 13: "Ребенок"
#    - Если 13-17: "Подросток"
#    - Если 18-65: "Взрослый"
#    - Если > 65: "Пенсионер"
# 3. Вызовите функцию для возрастов: 8, 15, 25, 70
#
# Пример:
# get_age_category(8) → "Ребенок"
# get_age_category(15) → "Подросток"
# get_age_category(25) → "Взрослый"
# get_age_category(70) → "Пенсионер"


# def get_age_category(age):
#     if age < 13:
#         return "Ребенок"
#     elif 13 <= age <= 17:
#         return "Подросток"
#     elif 18 <= age <= 65:
#         return 'Взрослый'
#     elif age > 65:
#         return 'Пенсионер'
# print(get_age_category(8))
# print(get_age_category(15))
# print(get_age_category(25))
# print(get_age_category(70))