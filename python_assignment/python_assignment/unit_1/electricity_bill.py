# Program 4: Electricity Bill Generator
# This program calculates an electricity bill based on the number of units consumed.

print("===== ELECTRICITY BILL GENERATOR =====")

name = input("Enter consumer name: ")
consumer_no = input("Enter consumer number: ")
units = float(input("Enter electricity units consumed: "))

# Calculate the bill using slab rates.
if units <= 100:
    amount = units * 1.50
elif units <= 200:
    amount = (100 * 1.50) + ((units - 100) * 2.50)
elif units <= 500:
    amount = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
else:
    amount = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

# Add a fixed charge.
fixed_charge = 50
total_bill = amount + fixed_charge

print("\n===== ELECTRICITY BILL =====")
print("Consumer Name   :", name)
print("Consumer Number :", consumer_no)
print("Units Consumed  :", units)
print("Energy Charge   : Rs.", round(amount, 2))
print("Fixed Charge    : Rs.", fixed_charge)
print("Total Bill      : Rs.", round(total_bill, 2))
