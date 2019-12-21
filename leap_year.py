#Leap_Year

cont = "y"

while cont.lower() == 'y':

    year = int(input("Enter the year :"))

  
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
    
    cont = input("Do you want to check another Year? y/n:")
    if cont == "n":
        break


