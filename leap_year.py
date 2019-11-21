year = int(input("Enter the year :"))
def is_leap(year):
    pass
    a = "The entered year is Leap Year"
    b = "The entered year is not leap year"
    if year in range (1900,10**5):
        if year % 4 == 0:   
            if year % 100 == 0:
                if year % 100 == 0 and year % 400 == 0:                 
                    return a   
                return b 
            return a
        else:
            return b

print(is_leap(year))
