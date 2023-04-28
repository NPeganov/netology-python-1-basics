"""
Задание 3
Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить
соответствующий знак зодиака.

Пример работы программы:

Введите день:
30

Введите месяц:
Август
Результат:
Ваш знак зодиака: Дева

Введите день:
29

Введите месяц:
Октябрь
Результат:
Ваш знак зодиака: Скорпион

"""


from datetime import date
from common.digital_input import digital_input


def get_birth_date():
    birth_date = None
    while birth_date is None:
        day = None
        while day is None:
            day = digital_input("Enter the day: ")

            if day < 1 or day > 31:
                day = None
                print("Wrong enter")

        month = None
        while month is None:
            month = input("Enter the month: ").lower()
            if month == 'january':
                month = 1
            elif month == 'february':
                month = 2
            elif month == 'march':
                month = 3
            elif month == 'april':
                month = 4
            elif month == 'may':
                month = 5
            elif month == 'june':
                month = 6
            elif month == 'july':
                month = 7
            elif month == 'august':
                month = 8
            elif month == 'september':
                month = 9
            elif month == 'october':
                month = 10
            elif month == 'november':
                month = 11
            elif month == 'december':
                month = 12
            else:
                month = None
                print("Wrong enter")

        if (day >= 31 and month in [4, 6, 9, 11]) or (month == 2 and day > 29):
            day = month = None
            print("The day does not exist in the month. Wrong date, try again.")
        else:
            birth_date = date(year=2000, month=month, day=day)  # Год не имеет отношения к знаку зодиака, но от того,
            # является ли год високосным или нет, зависит наличие 29 февраля. Поэтому и было решено взять 2000 год:
            # и год високосный, и число красивое.

    return birth_date


def zodiac_sign(birth_date):
    sign = None
    if isinstance(birth_date, date):
        year = birth_date.year
        if date(year, 3, 21) < birth_date <= date(year, 4, 20):
            sign = 'Aries'
        elif date(year, 4, 21) < birth_date <= date(year, 5, 21):
            sign = 'Taurus'
        elif date(year, 5, 22) < birth_date <= date(year, 6, 21):
            sign = 'Gemini'
        elif date(year, 6, 22) < birth_date <= date(year, 7, 22):
            sign = 'Cancer'
        elif date(year, 7, 23) < birth_date <= date(year, 8, 21):
            sign = 'Leo'
        elif date(year, 8, 22) < birth_date <= date(year, 9, 23):
            sign = 'Virgo'
        elif date(year, 9, 24) < birth_date <= date(year, 10, 23):
            sign = 'Libra'
        elif date(year, 10, 24) < birth_date <= date(year, 11, 22):
            sign = 'Scorpio'
        elif date(year, 11, 23) < birth_date <= date(year, 12, 22):
            sign = 'Sagittarius'
        elif date(year, 12, 23) < birth_date <= date(year, 1, 20):
            sign = 'Capricorn'
        elif date(year, 1, 21) < birth_date <= date(year, 2, 19):
            sign = 'Aquarius'
        else:
            sign = 'Pisces'
    else:
        sign = None
        print(f"Got invalid date object. Expected an instance of date class. Got: {birth_date}")

    return sign


if __name__ == '__main__':
    birth_date = get_birth_date()
    sign = zodiac_sign(birth_date)
    if sign:
        print(sign)
    # else:
        # Мы понимаем, что zodiac_sign может вернуть None, но мы точно знаем, что в этом примере такого не случится.
