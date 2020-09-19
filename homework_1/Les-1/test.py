while True:
    user_a = input('введите целое число результата в первый день\n')
    if user_a.isdigit():
        user_a = int(user_a)
        break
    else:
        print('ошибка ввода, это не число')

while True:
    user_b = input('введите целое число желаемый результат\n')
    if user_b.isdigit():
        user_b = int(user_b)
        break
    else:
        print('ошибка ввода, это не число')

day = 1
tmp = user_a
while tmp < user_b:
    tmp *= 1.1
    day += 1

print(day)
