# Program 1: Student Information and Academic Summary
# This program accepts student details and marks and displays an academic summary.

print("===== STUDENT INFORMATION AND ACADEMIC SUMMARY =====")

name = input("Enter student name: ")
usn = input("Enter USN: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

print("\nEnter marks for five subjects:")
mark1 = float(input("Subject 1: "))
mark2 = float(input("Subject 2: "))
mark3 = float(input("Subject 3: "))
mark4 = float(input("Subject 4: "))
mark5 = float(input("Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== ACADEMIC SUMMARY =====")
print("Name     :", name)
print("USN      :", usn)
print("Branch   :", branch)
print("Semester :", semester)
print("Total    :", total)
print("Average  :", round(average, 2))
print("Grade    :", grade)
