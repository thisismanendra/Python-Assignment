# Program 2: Factorial Using a Loop
# The factorial of n is the product of all positive integers from 1 to n.

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of", number, "=", factorial)
