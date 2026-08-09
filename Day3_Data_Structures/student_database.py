students = [
    {
        "id": 101,
        "name": "Yashraj",
        "department": "Data Science",
        "cgpa": 8.7
    },
    {
        "id": 102,
        "name": "Priya",
        "department": "Computer Science",
        "cgpa": 9.2
    },
    {
        "id": 103,
        "name": "Rahul",
        "department": "Data Science",
        "cgpa": 7.9
    },
    {
        "id": 104,
        "name": "Neha",
        "department": "Artificial Intelligence",
        "cgpa": 8.9
    }
]

print("=" * 65)
print("             STUDENT DATABASE ANALYZER")
print("=" * 65)

for student in students:
    print(
        f"ID: {student['id']} | "
        f"Name: {student['name']} | "
        f"Department: {student['department']} | "
        f"CGPA: {student['cgpa']}"
    )

topper = max(students, key=lambda student: student["cgpa"])

average_cgpa = sum(
    student["cgpa"] for student in students
) / len(students)

print("\n" + "-" * 65)
print(f"Top Student     : {topper['name']}")
print(f"Highest CGPA    : {topper['cgpa']}")
print(f"Average CGPA    : {average_cgpa:.2f}")

data_science_students = [
    student["name"]
    for student in students
    if student["department"] == "Data Science"
]

print(f"Data Science Students: {', '.join(data_science_students)}")
print("=" * 65)