# import requests

# url = 'https://dog.ceo/api/breeds/image/random'

# dogs = []  

# for i in range(10):
#     r = requests.get(url)
#     data = r.json()          
#     dogs.append(data['message'])  


# with open('dogs.txt', 'w') as file:
#     for dog in dogs:
#         file.write(dog + '\n')

# print("Полученные ссылки:")
# print("\n".join(dogs))

# 1. Используя API: https://dog.ceo/api/breed/random/image
# 2. Получите 5 случайных фотографий собак
# 3. Сохраните ссылки в файл 'random_dogs.txt'
# 4. Выведите на экран каждую ссылку с номером
#
# API: https://dog.ceo/api/breed/random/image
# Ответ: {"message": "https://...", "status": "success"}
#
# Ожидаемый результат:
# 1. https://images.dog.ceo/breeds/affenpinscher/...
# 2. https://images.dog.ceo/breeds/african/...
# 3. https://images.dog.ceo/breeds/airedale/...
# 4. https://images.dog.ceo/breeds/akita/...
# 5. https://images.dog.ceo/breeds/appenzeller/...
#
#  5 собак сохранено в random_dogs.txt


# import requests

# url = 'https://dog.ceo/api/breed/random/image'
# dog_links = []

# for i in range(5):
#     r = requests.get(url)
#     data = r.json()
#     link = data['message']
#     dog_links.append(link)
#     print(f"{i+1}. {link}")

# with open('random_dogs.txt', 'w') as file:
#     for link in dog_links:
#         f.write(link + '\n')

# print("5 собак сохранено в random_dogs.txt")






# 1. Используя API: https://dog.ceo/api/breeds/list/all
# 2. Получите список всех пород собак
# 3. API вернет словарь где ключи - породы, значения - подпороды
# 4. Выведите первые 10 пород
# 5. Подсчитайте всего пород
# 6. Сохраните в файл 'all_breeds.txt' в формате:
#    1. affenpinscher
#    2. african
#    3. airedale
#    и т.д.
#
# API: https://dog.ceo/api/breeds/list/all
# Ответ: {"message": {"affenpinscher": [], "african": [], ...}, "status": "success"}
#
# Ожидаемый результат:
# Первые 10 пород:
# 1. affenpinscher
# 2. african
# ...
# Всего пород: 197
# ✓ Все породы сохранены в all_breeds.txt
   
# import requests

# url = "https://dog.ceo/api/breeds/list/all"
# r = requests.get(url)
# data = r.json()

# breeds = list(data["message"].keys())

# print("Первые 10 пород:")
# for i, breed in enumerate(breeds[:10], 1):
#     print(f"{i}. {breed}")

# print(f"Всего пород: {len(breeds)}")

# with open('all_breeds.txt', 'w') as file:
#     for i, breed in enumerate(breeds, 1):
#         file.write(f"{i}. {breed}\n")

# print("✓ Все породы сохранены в all_breeds.txt")




# 1. Попросите пользователя ввести название породы
# 2. Используя API: https://dog.ceo/api/breed/{breed}/images
# 3. Получите все фотографии этой породы
# 4. Выведите количество фотографий
# 5. Выведите первые 5 ссылок
# 6. Сохраните все ссылки в файл 'breed_photos.txt'
#
# API: https://dog.ceo/api/breed/labrador/images
# Ответ: {"message": ["https://...", "https://...", ...], "status": "success"}
#
# Пример использования:
# Введите породу: labrador
# Найдено 297 фотографий
# Первые 5:
# 1. https://images.dog.ceo/breeds/labrador/n02099712_1003.jpg
# 2. https://images.dog.ceo/breeds/labrador/n02099712_1004.jpg
# ...
# ✓ 297 фотографий сохранено в breed_photos.txt


# import requests

# breed = input("Введите породу: ").lower()

# url = f"https://dog.ceo/api/breed/{breed}/images"
# r = requests.get(url)
# data = r.json()

# if data["status"] != "success":
#     print("Ошибка: такой породы нет!")
# else:
#     photos = data["message"]
#     print(f"Найдено {len(photos)} фотографий")

#     print("Первые 5:")
#     for i, link in enumerate(photos[:5], 1):
#         print(f"{i}. {link}")

#     with open("breed_photos.txt", "w") as f:
#         for link in photos:
#             f.write(link + "\n")

#     print(f"✓ {len(photos)} фотографий сохранено в breed_photos.txt")



# 1. Создайте список пород: ['labrador', 'golden', 'husky', 'bulldog', 'poodle']
# 2. Для каждой породы получите количество фотографий
# 3. Используйте API: https://dog.ceo/api/breed/{breed}/images
# 4. Выведите результаты в формате таблицы:
#    Порода          | Кол-во фотографий
#    ─────────────────────────────────
#    labrador        | 297
#    golden          | 218
#    ...
# 5. Найдите породу с максимальным и минимальным количеством фото
# 6. Сохраните результаты в файл 'breeds_comparison.txt'
#
# Ожидаемый результат:
# Порода          | Кол-во фотографий
# ─────────────────────────────────
# labrador        | 297
# golden          | 218
# husky           | 272
# bulldog         | 112
# poodle          | 286
#
# Максимум: labrador (297 фотографий)
# Минимум: bulldog (112 фотографий)
# ✓ Результаты сохранены в breeds_comparison.txt

# import requests

# breeds = ['labrador', 'golden', 'husky', 'bulldog', 'poodle']
# results = {}

# for breed in breeds:
#     url = f"https://dog.ceo/api/breed/{breed}/images"
#     r = requests.get(url)
#     photos = r.json()["message"]
#     results[breed] = len(photos)

# print("Порода          | Кол-во фотографий")
# print("-" * 35)

# for breed, count in results.items():
#     print(f"{breed:<15} | {count}")

# max_breed = max(results, key=results.get)
# min_breed = min(results, key=results.get)

# print(f"\nМаксимум: {max_breed} ({results[max_breed]} фотографий)")
# print(f"Минимум: {min_breed} ({results[min_breed]} фотографий)")

# with open("breeds_comparison.txt", "w") as f:
#     f.write("Порода          | Кол-во фотографий\n")
#     f.write("-" * 35 + "\n")
#     for breed, count in results.items():
#         f.write(f"{breed:<15} | {count}\n")
#     f.write(f"\nМаксимум: {max_breed} ({results[max_breed]})\n")
#     f.write(f"Минимум: {min_breed} ({results[min_breed]})\n")

# print("✓ Результаты сохранены в breeds_comparison.txt")


#    - bulldog (3 подпороды): french, staffordshire
#    - poodle (3 подпороды): miniature, standard, toy
#    - shepherd (3 подпороды): german, shetland
#    ...
# 5. Подсчитайте:
#    - Сколько пород БЕЗ подпород
#    - Сколько пород С подпородами
#    - Всего подпород
# 6. Сохраните отчет в файл 'breeds_report.txt'
#
# API: https://dog.ceo/api/breeds/list/all
# Ответ: {"message": {"affenpinscher": [], "bulldog": ["french", ...], ...}, "status": "success"}
#
# Ожидаемый результат:
# ═══════════════════════════════════════════
# ОТЧЕТ О ПОРОДАХ СОБАК
# ═══════════════════════════════════════════
#
# Породы С подпородами:
# - bulldog (2 подпороды): french, staffordshire
# - poodle (3 подпороды): miniature, standard, toy
# - shepherd (2 подпороды): german, shetland
# ...
#
# ═══════════════════════════════════════════
# СТАТИСТИКА:
# Всего пород: 197
# Пород БЕЗ подпород: 156
# Пород С подпородами: 41
# Всего подпород: 128
# ═══════════════════════════════════════════
#
# ✓ Отчет сохранен в breeds_report.txt

# import requests

# url = "https://dog.ceo/api/breeds/list/all"
# r = requests.get(url)
# data = r.json()["message"]

# with_sub = {breed: subs for breed, subs in data.items() if subs}
# without_sub = [breed for breed, subs in data.items() if not subs]

# total_subbreeds = sum(len(subs) for subs in with_sub.values())

# report = []

# report.append("══════════════════════════════════════")
# report.append("ОТЧЕТ О ПОРОДАХ СОБАК")
# report.append("══════════════════════════════════════\n")

# report.append("Породы С подпородами:")
# for breed, subs in with_sub.items():
#     subs_list = ", ".join(subs)
#     report.append(f"- {breed} ({len(subs)} подпороды): {subs_list}")

# report.append("\n══════════════════════════════════════")
# report.append("СТАТИСТИКА:")
# report.append(f"Всего пород: {len(data)}")
# report.append(f"Пород БЕЗ подпород: {len(without_sub)}")
# report.append(f"Пород С подпородами: {len(with_sub)}")
# report.append(f"Всего подпород: {total_subbreeds}")
# report.append("══════════════════════════════════════")

# with open("breeds_report.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(report))

# print("✓ Отчет сохранен в breeds_report.txt")
