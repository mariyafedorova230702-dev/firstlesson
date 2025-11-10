print ('hello world')

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Сумма:", num1 + num2)
print("Разность:", num1 - num2)
print("Произведение:", num1 * num2)
print("Деление:", num1 / num2)



number = int(input("Введите число: "))
divisor = int(input("Введите делитель: "))

remainder = number % divisor
print("Остаток от деления:", remainder)

base = int(input("Введите основание: "))
power = int(input("Введите степень: "))

result = base ** power
print(f"{base} в степени {power} = {result}")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Первое число больше:", num1 > num2)
print("Первое число меньше:", num1 < num2)
print("Числа равны:", num1 == num2)

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

full_name = first_name + " " + last_name
print("Полное имя:", full_name)
print("Количество символов:", len(full_name))


age = int(input("Введите ваш возраст: "))

print("Через 5 лет вам будет:", age + 5)
print("Через 10 лет вам будет:", age + 10)
print("Через 20 лет вам будет:", age + 20)

number = int(input("Введите число: "))

if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

kzt = int(input("Введите сумму в тенге: "))

usd = kzt / 500
print(f"{kzt} KZT = {usd} USD")

length = int(input("Введите длину: "))
width = int(input("Введите ширину: "))

area = length * width
perimeter = 2 * (length + width)

print("Площадь:", area)
print("Периметр:", perimeter)

age = int(input("Введите ваш возраст: "))

if age >= 18:
    print("Вы можете голосовать!")
else:
    print("Вам еще рано голосовать")


    