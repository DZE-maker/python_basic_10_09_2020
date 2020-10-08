prod_tamp = {'Название': ("введите название товара", str),
             'Цена': ("Стоимость", int),
             'В наличие': ("сейчас на складе", int),
             'единица измерения':("Единица измерения шт, кг ", str)}
auto_inc = 1

next_enter = True
prod_list = []
prod = {}
while  next_enter:
    for key, value in prod_tamp.items():
        user_value = input(f'{value[0]}\n')
        user_value = value[1](user_value)
        prod[key] = user_value
    prod_list.append((auto_inc, prod))
    auto_inc+=1
    while True:
        add_next = input("Хоттет ввести новый продукт? Да/нет")
        if add_next.lower() in ('да', 'нет'):

            next_enter = add_next.lower() == 'да'
            break
        else:
            print("не верный ввод")

print(prod_list)


for key, value in prod_list:
    print(key, value)