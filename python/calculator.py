import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def square_root(a):
    if a < 0:
        return "Error: Square root of a negative number is not allowed."
    return math.sqrt(a)

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Square Root (√)")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ")
        
        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))

        elif choice == '5':
            num = float(input("Enter a number: "))
            print("Result:", square_root(num))

        else:
            print("Invalid input. Please choose a valid operation.")

# Run the calculator
calculator()
