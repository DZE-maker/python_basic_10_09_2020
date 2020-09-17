"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
"""
while True:
    user_num = input("Введите число\n")
    if user_num.isdigit():
        break
    else:
        print("Ошибка ввода, введите число")
result = 9
while result:
    if str(result) in user_num:
        break
    result -= 1
print(result)