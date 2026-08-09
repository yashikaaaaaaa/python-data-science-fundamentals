print("=" * 50)
print("      STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 50)

name = input("Enter Student Name: ")

python = float(input("Python Marks: "))
sql = float(input("SQL Marks: "))
ml = float(input("Machine Learning Marks: "))

total = python + sql + ml
average = total / 3

if average >= 90:
    grade = "A+"
    remark = "Outstanding"
elif average >= 80:
    grade = "A"
    remark = "Excellent"
elif average >= 70:
    grade = "B"
    remark = "Very Good"
elif average >= 60:
    grade = "C"
    remark = "Good"
elif average >= 50:
    grade = "D"
    remark = "Needs Improvement"
else:
    grade = "F"
    remark = "Fail"

print("\n" + "=" * 50)
print("STUDENT REPORT")
print("=" * 50)

print(f"Student : {name}")
print(f"Total   : {total}")
print(f"Average : {average:.2f}")
print(f"Grade   : {grade}")
print(f"Remark  : {remark}")

print("=" * 50)