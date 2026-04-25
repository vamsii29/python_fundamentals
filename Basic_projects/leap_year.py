def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def main():
    year = int(input("Enter a year to check: "))
    print(leap_year(year))


main()