# 1. Создайте лотерею, где нужно угадать 5 случайных чисел от 1 до 50
# 2. Используя random.randint(), сгенерируйте 5 выигрышных чисел
# 3. Просите пользователя ввести 5 чисел
# 4. Сравните введенные числа с выигрышными
# 5. Выведите сколько чисел угадал пользователь
# Пример: "Вы угадали 3 из 5 чисел!"

# import random

# winning_games = []
# i = 0
# while i<5:
#     winning_games.append(random.randint(1,50))
#     i += 1

# print('Лотерея! Угадайте 5 чисел от 1 до 50: ')
# i =0
# usser_numbers = []
# while  i<5:
#     num = (int(input(f'Введите число: {1+i}:')))
#     usser_numbers.append(num)
#     i += 1
# matches = 0
# for num in usser_numbers:
#     if num in winning_games:
#         matches+=1

# print('Выигрышные числа: ',winning_games)
# print('Ваши числа: ', usser_numbers)
# print('Вы угадали',matches,'из 5!')




# 1. Создайте список предметов: ['Математика', 'Физика', 'История', 'Английский', 'Биология']
# 2. Используя random.shuffle(), перемешайте предметы
# 3. Выведите расписание на день в формате:
#    "1. Математика"
#    "2. Физика"
#    и т.д.
# 4. Спросите пользователя хочет ли он еще расписание (да/нет)
# 5. Если да - повторите, если нет - выход
# import random
# predmets = ['Математика', 'Физика', 'История', 'Английский', 'Биология']
# while True:
#     random.shuffle(predmets)
#     print(predmets)
#     print("\nВаше расписание на день: ") 
#     i =1
#     for  predmet in predmets:
#         i += 1
#         print(f"{i}-{predmet}")
#     answer = input('\nхотите новое расписание? (да/нет):').lower()
#     if answer == 'нет':
#         break


# 1. Есть список участников: ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# 2. Есть список призов: ['Ноутбук', 'Смартфон', 'Наушники', 'Монитор', 'Клавиатура']
# 3. Используя random.choice(), выбирайте случайного участника и приз
# 4. Удаляйте выбранного участника из списка
# 5. Выводите с текущей датой и временем:
#    "[2024-01-15 14:30:45] Алиса выиграла Ноутбук"
# 6. Делайте паузу 2 секунды между розыгрышами
# 7. Повторяйте пока не закончатся все участники
# import random
# import datetime
# import time
# peoples = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# prizes = ['Ноутбук', 'Смартфон', 'Наушники', 'Монитор', 'Клавиатура']
# while len(peoples)>0:
#     winer = random.choice(peoples)
#     prize = random.choice(prizes)
#     peoples.remove(winer)

#     now = datetime.datetime.now()
#     full_time = now.strftime('%d-%m-%Y %H:%M:%S')
#     print(f"[{full_time}] {winer} выйграл(a) {prize}")
#     time.sleep(2)



# 1. Используя string.ascii_letters и string.digits, создайте случайный текст из 20 символов
# 2. Выведите этот текст на экран
# 3. Попросите пользователя перепечатать текст
# 4. Измерьте время используя time.time()
# 5. Проверьте совпадает ли введенный текст с оригиналом
# 6. Выведите результаты:
#    "Время: X.XX секунд"
#    "Правильность: Y%"
#    "Скорость: Z символов в секунду"

# import string
# import random
# import time

# syvols = string.ascii_letters + string.digits

# original_text = ""
# for _ in range(20):
#     original_text += random.choice(syvols)
# print('Ваш текст для печати:')
# print(original_text)
# start_time = time.time()

# user_input = input('Введите текст: ')
# end_time = time.time()
# result_time = end_time - start_time

# correct_letter = 0
# for i in range(min(len(original_text),len(user_input))):
#     if original_text[i] == user_input[i]:
#         correct_letter += 1

# correct = (correct_letter/len(original_text)) * 100 
# speed = len(user_input)/ result_time 

# print(f'время : {result_time:.2f}')
# print(f'Правильность: {correct} %')
# print(f'Скорость : {speed:.1f} символов в секунду')



# 1. Попросите пользователя ввести желаемую длину пароля (минимум 8)
# 2. Используя string.ascii_letters, string.digits и string.punctuation:
#    - Создайте строку со всеми возможными символами
# 3. Используя random.choice(), сгенерируйте пароль нужной длины
# 4. Повторяйте генерацию пока пользователь не будет доволен (спросите да/нет)
# 5. Когда пароль выбран, выведите его
# Пример:
#    "Длина пароля: 12"
#    "Пароль: aB3$xKm9!Qp2"
#    "Нравится? (да/нет): "

# import string
# import random
# long_password = int(input('введи длину пароля минимум 8: '))
# while long_password < 8:
#     print('мало')
#     break

# all_symvols = string.ascii_letters + string.digits + string.punctuation

# while True:
#     password = ""
#     for _ in range(long_password):
#         password += random.choice(all_symvols)
#     print(f'пароль : {password}')
#     answer = input('нравится? да \ нет :').lower()   
#     if answer == 'да':
#         break  
# print('ваш пароль', password) 




# # 1. Используя datetime.datetime(), создайте дату: 1 января 2025 года
# # 2. В бесконечном цикле:
# #    - Получайте текущую дату и время
# #    - Вычисляйте разницу до Нового года
# #    - Выводите в формате: "Дней: X, Часов: X, Минут: X, Секунд: X"
# #    - Делаыыйте паузу 1 секунду
# # 3. Когда дата прошла, выведите "С Новым Годом!" и выход
# # Пример вывода: "Дней: 16, Часов: 09, Минут: 30, Секунд: 45"

# import datetime

# while True:
#     now = datetime.datetime.now()
#     new_year = datetime.datetime(2026, 1, 1 )
#     time_left = new_year - now
#     if time_left.total_seconds() <= 0:
#         print('с новым годом:! ')
#         break


# 1. Создайте файл 'students_unsorted.txt' с именами студентов:
#    "Виктор", "Алиса", "Боб", "Галина", "Дмитрий"
# 2. Прочитайте файл
# 3. Отсортируйте имена по алфавиту (.sort())
# 4. Запишите отсортированные имена в файл 'students_sorted.txt'
# 5. Выведите оба файла на консоль