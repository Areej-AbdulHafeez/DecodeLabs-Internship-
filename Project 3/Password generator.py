import random
import string

length = int(input("Enter password length : "))
password = ""
characters = string.ascii_letters + string.digits 

if length > 15:
    print("No password Exist")
else: 
     for i in range(length):
        password += random.choice(characters)
     print("Your password is:", password)
