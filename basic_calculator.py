#birsuyilmaz
def basic_calculator():
    operator = input("Please enter the operator that you would like to use (+, -, /, //, *, %): ")
    num1 = float(input("Please enter a num: "))
    num2 = float(input("Please enter another num: "))


    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            return num1 / num2
        case '//':
            return num1 // num2
        case '*':
            return num1 * num2
        case '%':
            return num1 % num2
        case _:
            return 'incomputable'

print("Welcome to the calculator\n")
while True:
    print("result:", basic_calculator())
    option = input("If you would like to continiue, enter c\nIf you would like to exit, enter e: ")
    if(option == 'e'):
        break

print("Thanks for using Luna Calculator\n")
#birsuyilmaz
