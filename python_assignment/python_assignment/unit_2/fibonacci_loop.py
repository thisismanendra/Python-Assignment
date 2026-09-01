# Program 3: Fibonacci Series Using a Loop
# Each Fibonacci number is the sum of the previous two numbers.

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number of terms.")
else:
    first = 0
    second = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(first, end=" ")
        next_term = first + second
        first = second
        second = next_term

    print()
