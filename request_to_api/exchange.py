# import requests
# from pprint import pprint

# # Ваш API ключ
# API_KEY = '76363498a0f076c9ff85e7de'

# # Базовая валюта
# base_currency = 'USD'

# # URL запроса
# url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}'

# response = requests.get(url)
# data = response.json()

# # Получаем все курсы
# conversion_rates = data['conversion_rates']

# # Получаем конкретный курс
# kzt_rate = conversion_rates['KZT']
# print(f'1 USD = {kzt_rate} KZT')

# # Конвертируем
# amount = 100
# result = amount * kzt_rate
# print(f'{amount} USD = {result} KZT')



# 1. Попросите пользователя ввести сумму в долларах (USD)
# 2. Используйте функцию exchange() для конвертации в 3 валюты:
#    - KZT (Казахстанский тенге)
#    - RUB (Российский рубль)
#    - EUR (Евро)
# 3. Выведите результаты в красивом формате
#
# Пример использования:
# Введите сумму в USD: 100
#
# ════════════════════════════════════════════════════════
#                   КОНВЕРТАЦИЯ $100
# ════════════════════════════════════════════════════════
# 100 USD (Доллар США)
#
# Конвертировано в:
# 1. 47545.00 KZT (Казахстанский тенге)
# 2. 9325.00 RUB (Российский рубль)
# 3. 92.00 EUR (Евро)

# CURRENCIES = {
#     'USD' : 'Доллар США',
#     'KZT' : 'Казахстанский тенге',
#     'RUB' : 'Российский рубль',
#     'EUR' : 'Евро',
#     }

# def exchange(amount, base='USD', target='KZT') :
#     url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()

#         if data['result'] == 'success':
#             rate = data['conversion_rates'][target]
#             return amount * rate
#         else:
#             print("Ошибка API")
#             return None
#     else:
#         print("Ошибка подключения.")
#         return None


# usd = float(input("Введите сумму в USD: "))    

# kzt = exchange(usd, 'USD', 'KZT')
# rub = exchange(usd, 'USD', 'RUB')
# eur = exchange(usd, 'USD', 'EUR')

# print("\n" + "=" * 60)
# print(f"        КОНВЕРТАЦИЯ ${usd} ")
# print ("=" * 60)

# print(f"{usd} USD ({CURRENCIES['USD']})\n")
# print("Конвертировано в:")

# print(f"1. {kzt:.2f} KZT ({CURRENCIES['KZT']})")
# print(f"2. {rub:.2f} RUB ({CURRENCIES['RUB']})")
# print(f"3. {eur:.2f} EUR ({CURRENCIES['EUR']})")



# 1. Покажите пользователю список доступных валют:
#    KZT, RUB, EUR, GBP, JPY, CNY, AED, INR
# 2. Попросите выбрать валюту
# 3. Попросите ввести сумму
# 4. Используйте функцию exchange() для конвертации в USD
# 5. Выведите результат с названием валют
#
# Пример использования:
# Доступные валюты:
# 1. KZT - Казахстанский тенге
# 2. RUB - Российский рубль
# 3. EUR - Евро
# 4. GBP - Британский фунт
# 5. JPY - Японская йена
# 6. CNY - Китайский юань
# 7. AED - Дирхам ОАЭ
# 8. INR - Индийская рупия
#
# Выберите валюту (введите номер): 1
# Введите сумму: 50000
#
# ════════════════════════════════════════════════════════
#                   КОНВЕРТАЦИЯ В USD
# ════════════════════════════════════════════════════════
# 50000.00 KZT (Казахстанский тенге)
#                    ↓
# 105.24 USD (Доллар США)
#
# Курс: 1 KZT = 0.00210 USD
# ═════════════════════════════════════════


# def exchange(amount, from_currency, to_currency):
#     url =f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
#     r = requests.get(url)
#     data = r.json()
#     return data['result'],data['info']['rate']

# CURRENCIES = {
#      1: ("KZT", "Казахстанский тенге"),
#     2: ("RUB", "Российский рубль"),
#     3: ("EUR", "Евро"),
#     4: ("GBP", "Британский фунт"),
#     5: ("JPY", "Японская йена"),
#     6: ("CNY", "Китайский юань"),
#     7: ("AED", "Дирхам ОАЭ"),
#     8: ("INR", "Индийская рупия"),
# }

# print("Доступные валюты:")
# for number , (code , name) in CURRENCIES.items():
#     print(f"{number}. {code} - {name}")

# choice = int(input("\nВыберите валюту (введите номер): "))
# if choice not in CURRENCIES:
#     print("Ошибка: такой валюты нет!")
#     exit()
# currency_code, currency_name = CURRENCIES[choice]   

# amount = float(input("Введите сумму:"))

# usd_value, rate = exchange(amount, currency_code, "USD")

# print("\n" + "═" * 60)
# print("                   КОНВЕРТАЦИЯ В USD")
# print("═" * 60)

# print(f"{amount:.2f} {currency_code} ({currency_name})")
# print(" " * 20 + "↓")
# print(f"{usd_value:.2f} USD (Доллар США)\n")

# print(f"Курс: 1 {currency_code} = {rate:.5f} USD")
# print("═" * 60)



# 1. Попросите пользователя ввести две валюты (коды: USD, KZT, EUR и т.д.)
# 2. Попросите ввести сумму
# 3. Используйте функцию exchange() для конвертации
# 4. Выведите курс обмена и результат конвертации
# 5. Обработайте ошибки если валюта не найдена
#
# Пример использования:
# Введите валюту ИЗ (например USD): EUR
# Введите валюту В (например KZT): JPY
# Введите сумму: 100
#
# ════════════════════════════════════════════════════════
#                КОНВЕРТАЦИЯ EUR → JPY
# ════════════════════════════════════════════════════════
# 100.00 EUR (Евро)
# Курс: 1 EUR = 150.50 JPY
#                    ↓
# 15050.00 JPY (Японская йена)
# ══════════════════════════════




# import requests

# # Функция конвертации
# def exchange(amount, from_currency, to_currency):
#     url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
#     response = requests.get(url)
#     data = response.json()

#     try:
#         result = float(data["result"])
#         rate = float(data["info"]["rate"])
#     except (KeyError, TypeError, ValueError):
#         return None, None

#     return result, rate

# # Словарь валют
# currencies = {
#     "USD": "Доллар США",
#     "KZT": "Казахстанский тенге",
#     "EUR": "Евро",
#     "GBP": "Британский фунт",
#     "RUB": "Российский рубль",
#     "JPY": "Японская йена",
#     "CNY": "Китайский юань",
#     "AED": "Дирхам ОАЭ",
#     "INR": "Индийская рупия"
# }


# print("Доступные валюты:")
# for i, (code, name) in enumerate(currencies.items(), start=1):
#     print(f"{i}. {code} - {name}")


# from_currency = input("\nВведите валюту ИЗ (например USD): ").strip().upper()
# if from_currency not in currencies:
#     print("Ошибка: валюта ИЗ не найдена!")
#     exit()

# to_currency = input("Введите валюту В (например KZT): ").strip().upper()
# if to_currency not in currencies:
#     print("Ошибка: валюта В не найдена!")
#     exit()


# amount = float(input("Введите сумму: "))


# result, rate = exchange(amount, from_currency, to_currency)
# if result is None:
#     print("Ошибка: валютная пара не найдена API!")
#     exit()


# print("\n" + "═" * 59)
# print(f"               КОНВЕРТАЦИЯ {from_currency} → {to_currency}")
# print("═" * 59)
# print(f"{amount:.2f} {from_currency} ({currencies[from_currency]})")
# print(f"Курс: 1 {from_currency} = {rate:.5f} {to_currency}")
# print(" " * 20 + "↓")
# print(f"{result:.2f} {to_currency} ({currencies[to_currency]})")
# print("═" * 59)
