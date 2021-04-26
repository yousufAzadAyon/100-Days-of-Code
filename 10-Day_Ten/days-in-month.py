def is_leapyear(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True    

    else:
        return False

def years_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year) and month == 2:
        return 29
    if month > 12 or month < 1:
        return 'Invalid month number!'
    return month_days[month - 1]

year = int(input('enter year: '))
month = int(input('enter month: '))
days = years_in_month(year, month)
print(days)