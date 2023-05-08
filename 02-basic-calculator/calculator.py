def add(number1, number2):
    result = number1 + number2
    print(str(number1) + " + " + str(number2) + " = " + str(result) + "\n")
    
def subtract(number1, number2):
    result = number1 - number2
    print(str(number1) + " - " + str(number2) + " =  " + str(result)+ "\n")

def multiply(number1, number2):
    result = number1 * number2
    print(str(number1) + " * " + str(number2) + " = " + str(result)+ "\n")

def division(number1, number2):
    result = number1 / number2
    print(str(number1) + " / " + str(number2) + " = " + str(result)+ "\n")

while True:
    
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("\nChoose the operation: ")

    if choice == "a" or choice == "A":
        print("Addition")
        number1 = int(input("Type your first number: "))
        number2 = int(input("Type your second number: "))
        add(number1, number2)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        number1 = int(input("Type your first number: "))
        number2 = int(input("Type your second number: "))
        subtract(number1, number2)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        number1 = int(input("Type your first number: "))
        number2 = int(input("Type your second number: "))
        multiply(number1, number2)

    elif choice == "d" or choice == "D":
        print("Division")
        number1 = int(input("Type your first number: "))
        number2 = int(input("Type your second number: "))
        division(number1, number2)

    else:
        print("Programm ended.")
        quit()