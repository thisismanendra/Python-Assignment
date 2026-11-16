# Program 1: Check Whether a Number is Prime or Not Prime
# A prime number has exactly two factors: 1 and itself.

number = int(input("Enter a number: "))

if number <= 1:
    print(number, "is Not Prime.")
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, "is Prime.")
    else:
        print(number, "is Not Prime.")
