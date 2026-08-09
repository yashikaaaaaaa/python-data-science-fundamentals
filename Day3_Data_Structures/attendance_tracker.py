students = {
    "Yashika",
    "Priya",
    "Rahul",
    "Neha",
    "Aman",
    "Arjun"
}

present = {
    "Yashika",
    "Priya",
    "Neha",
    "Aman"
}

absent = students - present
attendance_percentage = (len(present) / len(students)) * 100

print("=" * 55)
print("              ATTENDANCE ANALYZER")
print("=" * 55)

print(f"Total Students : {len(students)}")
print(f"Present        : {len(present)}")
print(f"Absent         : {len(absent)}")
print(f"Attendance     : {attendance_percentage:.2f}%")

print("\nPresent Students:")
for student in sorted(present):
    print("-", student)

print("\nAbsent Students:")
for student in sorted(absent):
    print("-", student)

print("=" * 55)