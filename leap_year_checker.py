#birsuyilmaz
def leap_year():
    print("!!Welcome to the Leap Year Calculator!!\n")
    year = int(input("Please enter the year you would like to check: "))
    if(year % 4 == 0):
        if((year % 100== 0) and (year % 400 != 0)):
            print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
        
leap_year()
#birsuyilmaz