# Program 4: Generate a Random OTP
# This program generates a random 4-digit or 6-digit OTP.

import random

print("===== RANDOM OTP GENERATOR =====")
print("1. Generate 4-digit OTP")
print("2. Generate 6-digit OTP")

choice = int(input("Enter your choice: "))

if choice == 1:
    otp = random.randint(1000, 9999)
    print("Your 4-digit OTP is:", otp)
elif choice == 2:
    otp = random.randint(100000, 999999)
    print("Your 6-digit OTP is:", otp)
else:
    print("Invalid choice.")
