# Program 3: Mathematical Calculator using Built-in Functions and Math Module
# This program demonstrates Python built-in functions and functions from math module.

import math

print("===== MATHEMATICAL CALCULATOR =====")

number = float(input("Enter a number: "))

print("\n===== BUILT-IN FUNCTIONS =====")
print("Absolute value :", abs(number))
print("Rounded value  :", round(number))
print("Integer value  :", int(number))

print("\n===== MATH MODULE FUNCTIONS =====")

if number >= 0:
    print("Square root    :", math.sqrt(number))
else:
    print("Square root    : Not defined for negative numbers")

print("Power (square) :", math.pow(number, 2))
print("Ceiling        :", math.ceil(number))
print("Floor          :", math.floor(number))

if number > 0:
    print("Natural log    :", math.log(number))
    print("Log base 10    :", math.log10(number))
else:
    print("Natural log    : Not defined")
    print("Log base 10    : Not defined")

print("Sine           :", math.sin(number))
print("Cosine         :", math.cos(number))
print("Tangent        :", math.tan(number))
