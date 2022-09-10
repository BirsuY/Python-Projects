#birsuyilmaz
def currency_converter():
    print("Welcome to the Currenc Converter Website!!!")
    print("This program currently only converts between USD and EURO\n")
    
    choice = input("Please enter if you would like to convert from USD or Euro: ")
    
    if(choice.lower() == 'usd'):
        dollars = eval(input("Please enter the amount of dollars you would like to convert: "))
        convert_to_euros = lambda dollars: dollars * 0.98
        print(f"{dollars}$ equals to {convert_to_euros(dollars)}€")
    elif(choice.lower() == 'euro'):
        euros = eval(input("Please enter the amount of euros you would like to convert: "))
        convert_to_dollars = lambda dollars: dollars * 1.02
        print(f"{euros}€ equals to {convert_to_dollars(euros)}$")
    else:
        print("Unfortunately we cannot convert from this currency!!!")
        
        
currency_converter()
#birsuyilmaz