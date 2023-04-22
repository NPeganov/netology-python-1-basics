def main(_year):
    if year % 4 == 0 and year % 100 != 0:
        print("The year is leap")
    else:
        print("The year is not leap")
    return _year


if __name__ == '__main__':
    print("Enter the year: ")
    year = int(input())
    main(year)
