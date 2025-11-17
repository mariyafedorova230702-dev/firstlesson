#list_input = input('enter 5 names: ')
#name = list_input.split()
#list_a = []
#list_b = []
#list_c = []
#if list_input.startswith('a'):
    #list_a = list_input.split()
#elif list_input.startswith('b'):
    #list_b = list_input.split()
#elif list_input.startswith('c'):
    #list_c = list_input.split()
#else:
    #list_names = list_input.split()
#print(list_a, list_b, list_c, list_names) 


#password = input('enter password: ')
#status = True
#if len(password) >=  8:
    #password
#else:
    #print("too short(((")
    #status = False

#if not password.isalpha():
    #pass
#else:
    #print('not nuber is bad')
    #status = False

#if password.istitle:
    #pass
#else:
    #print('')
    #status = False
#if status ==True:
    #naprint('all correct')



#name = input("enter your name and surname and fathername :")
#if len(name.split()) == 3:
    #name = name.title().split()
    #print(f"{name[0]} {name[1][0]}.{name[2][0]}.")
#else:
    #print('it s not fuul name(')
#print(len(name[0]))
#print(len(name[1]))   
#print(len(name[2]))

#n1 = name[0] [0]
#n2 = name [1] [0]
#n3 = name [2] [0]

#if n1 != n2 != n3:
    #print('start diffrend letters')
#else:
    #print("same")    



#a = [85, 92, 78, 95, 87, 90, 85]
#b = a.copy()
#b.sort()
##print(b)
#max = print("maks", b[-1])
#min = print("min",b[0])
#sred = (b[0] + b[2] + b[3] + b[4] + b[5] + b[6]/len(b))
#print(a.index(max))
#print(a.index(min))


# Создайте список слов: ['python', 'java', 'c++', 'javascript', 'go', 'rust']
# 1. Найдите слова, которые начинаются на 'j' (startswith + index)
# 2. Найдите слова с длиной > 4 символов (len)
# 3. Выведите первый символ каждого слова используя срезы [0]
# 4. Выведите все слова в верхнем регистре (upper)
# 5. Объедините все слова через ", " (join)
# 6. Возьмите срез первых 3 слов и объедините через " | "


# list_languech = ['python', 'java', 'c++', 'javascript', 'go', 'rust']
# if list_languech[0].startswith('j') and len(list_languech[0])>4:
#     print(list_languech[0])
# if list_languech[1].startswith('j') and len(list_languech[2])>4:
#     print(list_languech[1])
# if list_languech[2].startswith('j')and len(list_languech[3])>4:
#     print(list_languech[2])        
# if list_languech[3].startswith('j')and len(list_languech[3])>4:
#     print(list_languech[3])    
# if list_languech[4].startswith('j') and len(list_languech[4])>4:
#     print(list_languech[4])
# if list_languech[5].startswith('j') and len(list_languech[5])>4:
#     print(list_languech[5])         
# print( list_languech[0][0],list_languech[1][0],list_languech[2][0],list_languech[3][0],list_languech[4][0],list_languech[5][0])
# print(', '.join(list_languech).title)
# print('| '.join(list_languech[0:3]))


# Попросите пользователя ввести текст
# 1. Проверьте, начинается ли текст с заглавной буквы
# 2. Замените все пробелы на подчеркивания (replace)
# 3. Выведите текст в верхнем регистре
# 4. Выведите первое слово текста (split()[0] или срез)
# 5. Выведите последнее слово текста (split()[-1])
# 6. Подсчитайте количество слов (len(split()))
# 7. Объедините первое и последнее слово через " - "
# text = input('enret text: ')

# if text[0] == text[0].upper():
#     print('start big leters')
# else:
#     print('starts littel')
# print(text.replace(' ', '-'))
# print(text.upper())
# words = text.split()
# print(words[0])
# print(words[-1])
# print(len(words))
# print('-'.join([words[0], words[-1]]))



# Создайте список цен: [150, 200, 175, 300, 250, 180, 220]
# 1. Найдите товар дороже 200 (используйте условие)
# 2. Выведите количество товаров с ценой от 180 до 250 (условие + len среза)
# 3. Выведите самый дорогой товар (max) и его позицию (index)
# 4. Отсортируйте цены (sort)
# 5. Выведите первые 3 самые дешевые (срез [0:3])
# 6. Выведите последние 2 самые дорогие (срез [-2:])
# 7. Вычислите общую стоимость (sum)
# 8. Вычислите среднюю стоимость (sum / len)


# prise = [150, 200, 175, 300, 250, 180, 220]

# if prise[0] > 200:
#     print(prise[0])
# if prise[1] > 200:
#     print(prise[1])
# if prise[2] > 200:
#     print(prise[2])
# if prise[3] > 200:
#     print(prise[3])
# if prise[4] > 200:
#     print(prise[4])
# if prise[5] > 200:
#     print(prise[5])
# if prise[6] > 200:
#     print(prise[6])                        
# else:
#     ('not prise > 200')

# if 180<= prise[0] <= 200:
#     print(prise[0]) 
# if 180<= prise[1] <= 200:
#     print(prise[1]) 
# if 180<= prise[2] <= 200:
#     print(prise[2]) 
# if 180<= prise[3] <= 200:
#     print(prise[3]) 
# if 180<= prise[4] <= 200:
#     print(prise[4]) 
# if 180<= prise[5] <= 200:
#     print(prise[5])
# if 180<= prise[6] <= 200:
#     print(prise[6])
# else:
#     print('not ot 180 do 200')

# max_price = max(prise)
# position = prise.index(max_price)
# print('max prise: ', max_price,' position: ', position)
# prise.sort()
# print(prise)
# print(prise[0 : 3])
# print(prise[-2: ])
# sum = sum(prise)
# print(sum)
# srednya = sum / len(prise)
# print(srednya)


# Создайте список логинов: ['admin123', 'user_2024', 'test@mail', 'john_doe', 'alex.smith']
# 1. Проверьте, сколько логинов содержат подчеркивание (count('_'))
# 2. Проверьте, сколько логинов содержат точку (count('.'))
# 3. Найдите самый длинный логин (max(*, key=len) ИЛИ через список длин)
# 4. Выведите первый символ каждого логина используя срезы
# 5. Замените все '@' на '#' в каждом логине
# 6. Найдите логины, которые начинаются с буквы 'a' или 'u' (startswith)
# 7. Выведите все логины в верхнем регистре
# 8. Объедините все логины через " | "


# spisok_loginov = ['admin123', 'user_2024', 'test@mail', 'john_doe', 'alex.smith']
# if spisok_loginov[0].count('_'):
#     print('have _: ', spisok_loginov[0])
# if spisok_loginov[2].count('_'):
#     print('have _: ', spisok_loginov[2])
# if spisok_loginov[3].count('_'):
#     print('have _: ', spisok_loginov[3])
# if spisok_loginov[4].count('_'):
#     print('have _: ', spisok_loginov[4])
# if spisok_loginov[5].count('_'):
#     print('have _: ', spisok_loginov[5])    
        



# Создайте список данных: [18, 'Александр', 92, True, 'ACTIVE']
# (возраст, имя, балл, активный, статус)
# 1. Проверьте возраст >= 18 И статус == 'ACTIVE'
# 2. Если оба условия верны - "Студент принят"
# 3. Выведите имя в формате "А.****" (используйте срезы и len)
# 4. Определите категорию по баллу:
#    - Если балл >= 90: "Отличник"
#    - Если балл >= 75: "Хорошист"
#    - Иначе: "Нужна помощь"
# 5. Переведите статус в нижний регистр и проверьте == 'active'

# data =  [18, 'Александр', 92, True, 'ACTIVE']
# age = data[0]
# name = data[1]
# bal = data[2]
# activ = data[3]
# statuse = data[4]

# if age <= 18 and statuse == 'ACTIVE' :
#     print('vse super, ty prinyt')
# else:
#     print('vy nam ne podhodite')

# if 90 <= bal <= 100:
#     print('ty otlichnic')
# elif 75 <= bal <= 89:
#     print('ty hotoshist')
# else:
#     print('van nuzhna pomosh')


# statuse_lower = statuse.lower()

# if statuse_lower == 'active':
#     print ('status podtverzhden', statuse_lower)
# else:
#     print('status ne podtvezhden', statuse_lower)    


# Попросите пользователя ввести список товаров через запятую
# Пример: "молоко, хлеб, яйца, масло, сыр"
# 
# 1. Разделите на список товаров (split(', '))
# 2. Капитализируйте каждый товар (капитализируйте вручную через присваивание или вывод)
# 3. Выведите количество товаров (len)
# 4. Отсортируйте товары (sort)
# 5. Выведите первые 2 товара (срез [0:2])
# 6. Выведите последний товар (срез [-1] или [-1:])
# 7. Найдите товар с самым длинным названием (используйте max или условие)
# 8. Объедините товары обратно через " | "
# 9. Замените все пробелы на подчеркивания в объединенной строке
# 10. Выведите финальный результат в верхнем регистре    


spisok = input('vvedi spisok pokupok cher zapyatu 5 shtuk: ')
item = spisok.split(',')
item0 = item[0].capitalize()
item1 = item[1].capitalize()
item2 = item[2].capitalize()
item3 = item[3].capitalize()
item4 = item[4].capitalize()
