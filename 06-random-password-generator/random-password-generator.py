import string
import random

characters = list(string.ascii_letters + string.digits + "!@#%^&*()")

def generate_password():
    password_length = int(input("What's the lenght of your password would you like to be? "))

    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    password = "".join(password)

    print(password)

choice = input("Would you like to generate a password? (Yes/No) ")

if choice == "Yes" or choice == "yes":
    generate_password()
elif choice == "No" or choice == "no":
    print("The program ended.")
    quit()
else:
    print("Invalid option, please choose Yes or No.")
    quit()