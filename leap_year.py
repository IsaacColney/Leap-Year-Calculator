
year = input("Enter the year :")

if year != int():
    print ('Input integer only!!!!')
    year = int(input("Enter the year :"))
else:
    is_leap(year)
    
def is_leap(year):
    pass
    a = "The entered year is Leap Year"
    b = "The entered year is not leap year"
    if year % 4 == 0:   
        if year % 100 == 0:
            if year % 100 == 0 and year % 400 == 0:                 
                return a   
            return b 
        return a
    else:
        return b
    
print(is_leap(year))

input("Press any Key to close.......")
