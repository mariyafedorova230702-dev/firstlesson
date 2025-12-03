# import requests
# from config import OPEN_WEATER_MAP_API_KEY
# from pprint import pprint
# from datetime import datetime
# import time


# city_name = input("Введите город (по умолчанию Алматы): ").strip()
# if city_name == "":
#     city_name = "Алматы"
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPEN_WEATER_MAP_API_KEY}'
# r = requests.get(url)

# print(r.status_code)


# data = r.json()
# print("\n==============================")
# print(f"🌎 {data['name']}, {data['sys']['country']}")
# print(f"📍 Координаты: {data['coord']['lat']}°N, {data['coord']['lon']}°E")
# print("==============================\n") 



# temp = data['main']['temp'] - 273.15
# feels_like = data['main']['feels_like'] - 273.15
# temp_min = data['main']['temp_min'] - 273.15
# temp_max = data['main']['temp_max'] - 273.15


# print(f"🌡 Температура: {temp:.2f}°C (ощущается {feels_like:.2f}°C)")
# print(f"📊 Диапазон: {temp_min:.2f}°C — {temp_max:.2f}°C")
# print(f"💧 Влажность: {data['main']['humidity']}%")
# print(f"🌬 Давление: {data['main']['pressure']} гПа")

# wind_speed = data["wind"]["speed"]
# wind_deg = data["wind"]["deg"]
# print(f"🍃 Ветер: {wind_speed} м/с, направление {wind_deg}°")


# print(f"👁 Видимость: {data['visibility'] / 1000:.1f} км")
# print(f"☁️ Облачность: {data['clouds']['all']}%")


# print("\nПогодные условия:")
# for w in data['weather']:
#     print(f"• {w['main']}: {w['description']}")

# tz = data["timezone"] 
# print(f"""
# 🕒 Обновлено: {datetime.fromtimestamp(data["dt"] + tz).strftime("%Y-%m-%d %H:%M:%S")}
# 🌅 Восход: {datetime.fromtimestamp(data["sys"]["sunrise"] + tz).strftime("%H:%M")}
# 🌇 Закат: {datetime.fromtimestamp(data["sys"]["sunset"] + tz).strftime("%H:%M")}
# """)
    


