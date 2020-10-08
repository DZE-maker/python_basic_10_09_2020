"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль
"""

def my_division(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError as e:
        return "На ноль делить нельзя"

number_1 = float(input('Введите первое число'))
number_2 = float(input('Введите втоторе число'))
print(my_division(number_1, number_2))