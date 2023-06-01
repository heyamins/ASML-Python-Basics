
def is_leapyear(year):
    """Determine if a year is a leapyear"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# -----------------------------------------------------------------

print(2023, is_leapyear(2023))
print(2024, is_leapyear(2024))


# for year in [2023, 2024, 2100, 2000]:
#     print(year, is_leapyear(year))


jaar = int(input('Which year? : '))
print(jaar, is_leapyear(jaar))


import calendar
print(jaar, calendar.isleap(jaar))
