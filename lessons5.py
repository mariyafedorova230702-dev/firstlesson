# Создайте список слов: ['banana', 'apple', 'cherry', 'date', 'elderberry']
# 1. Отсортируйте слова по алфавиту
# 2. Разверните список в обратном порядке
# 3. Используя цикл, выведите каждое слово в верхнем регистре
# 4. Подсчитайте количество слов, которые начинаются на гласную

# words = ['banana', 'apple', 'cherry', 'date', 'elderberry']
# words.sort()
# print(words)
# print(words[::-1])
# for word in words:
#     print(word.upper())
# a = 0
# leters = 'aye'
# for word in words:
#     if word[0] in leters:
#         a+=1
#     print("na glasnuu: ", a)






# Создайте список текстов с пробелами: [' hello ', '  world  ', ' python ']
# 1. Используя цикл, удалите пробелы в начале и конце каждого слова
# 2. Замените все оставшиеся пробелы на подчеркивания
# 3. Переведите все в нижний регистр
# 4. Создайте новый список с очищенными данными

# words = [' hello ', '  world  ', ' python ']
# new_words =[]
# for word in words:
#    clean = word.strip()
#    clean.replace(' ','-')
#    clean.lower()
#    new_words.append(clean)
#    print(new_words)  

# Создайте список: [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# 1. Найдите индекс первого числа 5
# 2. Подсчитайте, сколько раз встречается 5
# 3. Используя цикл и индексы, выведите все позиции где стоит 5
# 4. Удалите первое вхождение 5
# 5. Выведите обновленный список

# nums = [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# index_5 = nums.index(5)
# print("index 5: ", index_5)
# cout_5 = nums.count(5)
# print("cout 5: ", cout_5)
# for i in range(len(nums)):
#     if i == 5:
#         print("vse position: ", i)
# nums.remove(5)
# print(nums)


# Создайте список студентов: ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# Используя range(len(...)):
# 1. Выведите всех студентов с их номерами (1, 2, 3, и т.д.)
# 2. Выведите номер студента 'Виктор'
# 3. Вставьте нового студента 'c' на позицию 2
# 4. Выведите обновленный список с номерами

# studets = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# for i in range(len(studets)):
#     print (i +1, studets[i] )
# for  i in range(len(studets)):
#     if i == 'Виктор':
#         print('nuber victor: ', i)
    
# studets.insert(1, 'Виктор')

# for i in range(len(studets)):
#     print(i +1, studets[i])

# Создайте список чисел: [2, 4, 6, 8, 10, 12, 15, 18, 20]
# 1. Создайте новый список, где каждое число умножено на 5
# 2. Создайте новый список, где каждое число возведено в квадрат
# 3. Создайте новый список только из чисел, которые делятся на 3
# 4. Объедините первые два списка в один
# Выведите все три новых списка


# nubers = [2, 4, 6, 8, 10, 12, 15, 18, 20]
# nums_x5 =[]
# nusm_kvad = []
# nums_del3 =[]
# for i in range(len(nubers)):
#     volue = nubers[i]
    
#     nums_x5.append(volue * 5)
#     print(nums_x5)

#     nusm_kvad.append(volue ** 2)
#     print(nusm_kvad)
#     if volue % 3:
#         nums_del3.append(volue)
#         print(nums_del3)
# togeser = nums_x5 + nusm_kvad
# print(togeser)        





# Создайте список слов: ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# 1. Найдите самое длинное слово
# 2. Найдите самое короткое слово
# 3. Используя цикл, выведите каждое слово с его:
#    - Первой буквой
#    - Последней буквой
#    - Длиной
# 4. Создайте новый список слов в верхнем регистре
# 5. Подсчитайте количество слов, которые содержат букву 'p'


# words = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']

# longer = words [0]
# for word in words:
#     if(len(word))>(len(longer)):
#         longer = word
# print('longer: ', longer )
# short = word[0]
# for word in words:
#     if(len(word))<len(short):
#         short = word
# print('short: ', short )

# for word in words :
#     print('first letter ',word[0], 'last letter: ', word[-1], 'long: ', len(word))

# for word in words:
#     upper = word.upper()
#     print(upper)    
# for word in words :
#     if word.count('p'):
#         print('count p: ', word)



# Создайте таблицу умножения для чисел от 2 до 5
# 1. Для каждого числа от 2 до 5 создайте его таблицу умножения (от 1 до 10)
# 2. Выведите таблицу в формате: "Таблица 2: 2 * 1 = 2, 2 * 2 = 4, ..."
# 3. Создайте список всех произведений
# 4. Подсчитайте количество произведений > 20 и < 30
# 5. Найдите максимальное произведение

# summ = []
# quantity = 0
# max_value = 0

# for n in range(2, 6):
#     print(f"tabl {n}")
#     for i in range(1, 11):
#         result = n * i
#         print(f"{i}*{n}= {result}")
#         summ.append(result)
#         print(summ)

#         if 20 < result < 30:
#             quantity += 1
#             print('ot 20 do 30:', quantity)
#         else:
#             pass
#         if  max_value < result:
#             max_value = result
# print("all summ: ", summ)
# print("ot 20 do 30", quantity)
# print("max value: ", max_value)


# Создайте список: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 1. Отсортируйте список
# 2. Разверните в обратном порядке
# 3. Подсчитайте все элементы
# 4. Подсчитайте сколько раз встречается число 5
# 5. Найдите индекс первого числа 1
# 6. Удалите первое число 1
# 7. Выведите список после каждой операции

# nubers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# nubers.sort()
# print(nubers)
# print(nubers[::-1])
# print(len(nubers))
# print(nubers.count(5))
# print(nubers.index(1))
# nubers.remove(1)
# print('удаление первого 1: ', nubers)

# Создайте список фраз:
# ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
# 1. Найдите все фразы, которые содержат букву 'о'
# 2. Создайте новый список фраз длиной > 20 символов
# 3. Замените все пробелы на подчеркивания в каждой фразе
# 4. Создайте новый список с первым словом каждой фразы
# 5. Подсчитайте общее количество слов во всех фразах
words = ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']
words_20 = []
first_word = []
total = 0
for word in words:
   if word.count('о'):
      print('содержит о: ',word)

for word in words:
   if len(word) > 20:
      words_20.append(word)
      print(words_20)

for word in words:
   print(word.replace(' ','-'))
        
for word in words:
   first_word.append(word.split()[0])
   print(first_word)

for word in words:
    total += len(word.split())
    print('общее количество слов:', total)


# Создайте списки:
# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c']
#
# 1. Создайте новый список, где каждое число соединено с каждой буквой
#    Результат: ['1a', '1b', '1c', '2a', '2b', '2c', ...]
#
# 2. Создайте новый список со строками "число-буква" для пар:
#    ['1-a', '2-b', '3-c', '4-?']
#    (если букв меньше, пропустите оставшиеся числа)
#
# 3. Для каждой пары выведите информацию
#
# 4. Используйте extend() для объединения списков

numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']
num_let = []
num_let2 = []
for num in numbers:
   for letter in letters:
      num_let.append(num + letter) 
      print(num_let)
   