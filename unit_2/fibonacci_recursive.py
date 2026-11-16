# Program 5: Fibonacci Series Using Recursion
# This program generates Fibonacci terms using a recursive function.

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number of terms.")
else:
    print("Fibonacci Series:")

    for i in range(n):
        print(fibonacci(i), end=" ")

    print()
