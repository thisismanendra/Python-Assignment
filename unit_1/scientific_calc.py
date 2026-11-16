# Program 2: Scientific Calculator for Two Numbers
# This program performs scientific-style operations on two numbers.

import math

print("===== SCIENTIFIC CALCULATOR FOR TWO NUMBERS =====")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square root of first number")
print("7. Square root of second number")
print("8. Logarithm of first number")
print("9. Logarithm of second number")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero is not allowed.")
elif choice == 5:
    print("Result =", a ** b)
elif choice == 6:
    if a >= 0:
        print("Result =", math.sqrt(a))
    else:
        print("Square root of a negative number is not real.")
elif choice == 7:
    if b >= 0:
        print("Result =", math.sqrt(b))
    else:
        print("Square root of a negative number is not real.")
elif choice == 8:
    if a > 0:
        print("Result =", math.log(a))
    else:
        print("Logarithm requires a positive number.")
elif choice == 9:
    if b > 0:
        print("Result =", math.log(b))
    else:
        print("Logarithm requires a positive number.")
else:
    print("Invalid choice.")
