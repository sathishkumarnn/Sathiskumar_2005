def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_user_input():
    year = int(input("Enter a year: "))
    return year

user_year = get_user_input()

if is_leap_year(user_year):
    print(f"{user_year} is a leap year!")
else:
    print(f"{user_year} is not a leap year.")
     