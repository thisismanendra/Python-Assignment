#Student Information and Academic information

print("--------- STUDENT INFORMATION AND ACADEMIC SUMMARY-------")
name = input("Enter Student name: ")
usn = input("Enter USN: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

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

print("\n------- STUDENT REPORT -------")
print("Name     :", name)
print("USN      :", usn)
print("Branch   :", branch)
print("Semester :", semester)
print("Total    :", total)
print("Average  :", round(average, 2))
print("Grade    :", grade)
