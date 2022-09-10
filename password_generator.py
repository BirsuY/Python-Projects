#birsuyilmaz
import string
import random

elements = list(string.ascii_letters + string.digits + string.punctuation)

def passwrd_generator(ans1):
    print("\nWelcome to the password generator app!!\n")
    passwords = {}
    passwrd = ""
    ans2 = input("\nWould you like to save your passwords(Y/N): ")
    while(ans1.lower() == 'y'):
        count = int(input("\nHow long you password should be: "))
        random.shuffle(elements)
        
        for i in range(count):
                passwrd += random.choice(elements) 
                     
        if(ans2.lower() =='y'):
            account = input("Please enter the name of the account: ")
            passwords[account] = passwrd
            print("This is your account and password information: ", passwords)
        else:
            print("This is your password: ", passwrd)
        
        ans1 = input("\nWould you like to geneate another password for your account(Y/N): ")
    
    
    print("\nThank you for using the password generator app!!")


ans1 = input("Would you like to geneate a password for your account(Y/N): ")
if(ans1.lower() == 'n'):
        print("\nThank you for prefering the password generator app!!")
        quit()
elif(ans1.lower() == 'y'):                      
    passwrd_generator(ans1)
else:
    print("This is an invalid answer\nProgram ended")
    quit()
            
#birsuyilmaz