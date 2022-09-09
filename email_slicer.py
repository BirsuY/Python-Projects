from distutils import extension


#birsuyilmaz
def email_slicer():
    email = input("Please enter the email: ")
    (user_name, domain)= email.split("@")
    (domain, extension)  = domain.split(".")
    return (user_name, domain, extension)
    

username, domain, extension = email_slicer()
print("Welcome to Luna Email Slicer Website")
print("Username:", username, "\nDomain:", domain, "\nExtension: ", extension)
#birsuyilmaz