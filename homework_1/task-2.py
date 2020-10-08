"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def user (name, surname, yyyy, city, email, phone):
    print(f" Имя - {name}; Фамилия - {surname}; Год - {yyyy}; Город - {city}; EMAIL - {email};  Телефон - {phone}")


user (name=str(input( "введите имя")), surname=str(input("введите фам")), yyyy=str(input("год")),
            city=str(input("Введите город")), email=str(input("Введите email")),
            phone=str(input("Введите номер телефона")))



"""



def user (name : str, surname : str , hhhh: int, city: str, mail: str, phone: int) -> str:
    try:
        name = str(input("Введите имя\n"))
        surname = str(input("Введите фамилию\n"))
        hhhh = int(input("Введите год рождения\n"))
        city = str(input("Введите город проживания\n"))
        mail = str(input("Введите ваш адрес электронной почты\n"))
        phone = int(input("Введите ващ номер телефона"))
    except ValueError:
        return name, surname, hhhh, city, mail, phone
name_1 = name

print(f"Имя - {name_1}; "
      f"фамилия - {surname_2}; "
      f"Год рождения - {hhhh_3}; "
      f"Город - {city_4}; "
      f"Электронная почта - {mail_5}"
      f"Телефон - {phone_6}")
"""