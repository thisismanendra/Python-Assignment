# Program 3: Mathematical Calculator using Built-in Functions and Math Module
# This program demonstrates Python built-in functions and functions from math module.

import math
print("\n--------- MATHEMATICAL OPERATOR -------")
num = float(input("Enter a number: "))
print("Number         :",num)
print("Absolute value :", abs(num))
print("Integer value  :", int(num))

if num >= 0:
    print("Square root    :", math.sqrt(num))
else:
    print("Square root    : Not defined for negative numbers")

print("Square :", num** 2)
print("Ceiling Value :", math.ceil(num))
print("Floor Value :", math.floor(num))
print("Cube :",num**3)
print("Type :",type(num))
print("Memory Address :",id(num))
