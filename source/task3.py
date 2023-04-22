from datetime import date


def get_birth_date():
    birth_date = None
    while birth_date is None:
        day = None
        while day is None:
            print("Enter the day: ")
            day = int(input())

            if 0 < day <= 31:
                break
            else:
                day = None
                print("Wrong enter")

        month = None
        while month is None:
            print("Enter the month: ")
            month = str(input())
            month = month.lower()
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

        if day >= 31 and month in [4, 6, 9, 11]:
            day = None
            month = None
        elif day > 29 and month == 2:
            day = None
            month = None
        else:
            birth_date = date(2000, month, day)

        if birth_date:
            break

    return birth_date


def zodiac_sign(birth_date):
    if date(2000, 3, 21) < birth_date <= date(2000, 4, 20):
        print('Aries')
    elif date(2000, 4, 21) < birth_date <= date(2000, 5, 21):
        print('Taurus')
    elif date(2000, 5, 22) < birth_date <= date(2000, 6, 21):
        print('Gemini')
    elif date(2000, 6, 22) < birth_date <= date(2000, 7, 22):
        print('Cancer')
    elif date(2000, 7, 23) < birth_date <= date(2000, 8, 21):
        print('Leo')
    elif date(2000, 8, 22) < birth_date <= date(2000, 9, 23):
        print('Virgo')
    elif date(2000, 9, 24) < birth_date <= date(2000, 10, 23):
        print('Libra')
    elif date(2000, 10, 24) < birth_date <= date(2000, 11, 22):
        print('Scorpio')
    elif date(2000, 11, 23) < birth_date <= date(2000, 12, 22):
        print('Sagittarius')
    elif date(2000, 12, 23) < birth_date <= date(2000, 1, 20):
        print('Capricorn')
    elif date(2000, 1, 21) < birth_date <= date(2000, 2, 19):
        print('Aquarius')
    else:
        print('Pisces')

    return birth_date


#if __name__ == '__main__':
birth_date = get_birth_date()
zodiac_sign(birth_date)
