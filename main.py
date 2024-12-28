# i = 0
# while i < 10:
#     print('Привет')
#     i += 1

#     num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())

# for i in range(101):
#     print(i)

# i = 0
# while i < 101:
#     print(i)
#     i += 1

# for i in range(0, 100, 3):
#     print(i)

# i = 0
# while i < 100:
#     print(i)
#     i += 3

#     text = input()
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input()

# print('Сумма чисел равна', total)

# i = 0
# total = 0
# while i < 10:
#     total += i

#     i = -1
# while i > 0:
#     print('Hello world!')

number = int(input("Введите число: "))
while number > 0:
    print(number, end=" ")
    number = 1

number = int(input("Введите число: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
print(f"Факториал числа {number} равен {factorial}")

number = input("Введите число: ")
sum_digits = i = 0
while i < len(number):
    sum_digits += int(number[i])
    i += 1
print(f"Сумма цифр числа {number} равна {sum_digits}")

name = input("Введите ваше имя: ")
i = 0
while i < len(name):
    print(name[i])
    i += 1