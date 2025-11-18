# num = 0
# while num < 10:
#     if num % 2 == 0:
#         print('четные: ', num)
#     num +=  1


   # Попросите пользователя ввести число N
# Выведите все числа от 1 до N
# Используйте while цикл

# n = int(input('введи число: '))
# while n >= 1:
#     print(n)
#     n -= 1

# Попросите пользователя ввести число N
# Выведите числа от N до 1 (в обратном порядке)
# Используйте while с уменьшением переменной

# n = int(input('введи число: '))
# i = 0
# while n >= i:
#     print(i) 
#     i += 1

# Попросите пользователя ввести число N
# Найдите сумму всех чисел от 1 до N
# Используйте while и накопление значений
# Выведите результат

# n = int(input('введи число: '))
# i = 1
# summ = 0
# while n >= i:
#     summ += i
#     i += 1
# print(summ)

# Создайте список: [10, 20, 30, 40, 50]
# Используя while и индексы, выведите:
# - Каждый элемент
# - Индекс элемента
# Формат: "Индекс 0: 10"

# numbers = [10, 20, 30, 40, 50]
# index = 0
# while index < len(numbers):
#     print(f'index{index}:{numbers[index]}')
#     index += 1


# Создайте список: ['Python', 'Java', 'C++', 'JavaScript', 'Go']
# Попросите пользователя ввести язык программирования
# Используя while, найдите этот язык в списке
# Если найден - выведите его индекс
# Если не найден - выведите "Язык не найден"

# words = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
# input_word = input('ввести язык программирования:')
# index = 0
# found = True
# while index < len(words):
#     if words[index] == input_word:
#         print('found languges! index: ', index)
#         found = True
#         break
#     index += 1
# else:
#     print(' not found')


# Попросите пользователя ввести число N
# Найдите произведение (умножение) всех чисел от 1 до N
# Используйте while цикл
# Пример: N=5 → 1*2*3*4*5 = 120

# number = int(input('enter number: '))
# i = 1
# total = 1

# while number >= i:
#     total *= i
#     i += 1
# print(total)    

# Попросите пользователя ввести два числа: start и end
# Найдите все четные числа между start и end
# Используйте while цикл
# Выведите каждое четное число и их количество

# start = int(input('enter start number: '))
# end = int(input('enter end number'))
# i = start
# count = 0
# while i <= end: 
#     if i % 2 == 0:
#         print('number % 2: ',i)
#         count += 1
#     i += 1
# print('count nuber % 2: ', count)        


# Правильный пароль: 'qwerty'
# Дайте пользователю 3 попытки введения пароля
# Используйте while с счетчиком попыток
# После каждой неудачной попытки выведите: "Попытка N из 3"
# Если угадал - "Пароль верный!"
# Если кончились попытки - "Доступ запрещен"

# correct_password = 'qwerty'
# popytka = 1
# while popytka <= 3:
#     input_password = input('enter paassword: ')
#     if input_password == correct_password:
#         print('Пароль верный!')
#         break
#     else:
#         print('попытка: ', popytka, 'из 3')
#     popytka += 1    
# if popytka > 3 and input_password != correct_password:
#     print('попытки изончились')    

# Попросите пользователя вводить числа
# Используя while, суммируйте только положительные числа
# Если пользователь введет 0 или отрицательное число - остановитесь
# Выведите итоговую сумму и количество введенных положительных чисел

# total = 0
# count = 0

# while True:
#     number = int(input('enter number: '))
#     if number <= 0:
#         break
#     total += number
#     count += 1
# print('сумма положительных: ', total)
# print('количество положительных', count)  
    

# Попросите пользователя ввести число N
# Используя while, уменьшайте это число в два раза
# Выведите каждое значение
# Остановитесь когда число станет меньше 1
# Пример: N=100 → 100, 50, 25, 12.5, 6.25, ...

N = int(input('enter nuber: ')) 
while N >= 1:
    print(N)
    N = N/2   
