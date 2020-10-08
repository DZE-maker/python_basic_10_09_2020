"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""

def itet(*args):
    prev = float('inf')
    for num in args:
        if num > prev:
            yield num
        prev = num
test = [-1, 3, 6, 12, -5, 0, 2, 7]
result = [itm for idx, itm in enumerate(test) if idx and itm > test[idx - 1]]
print(result)
assert result == [3, 6, 12, 0, 2, 7]