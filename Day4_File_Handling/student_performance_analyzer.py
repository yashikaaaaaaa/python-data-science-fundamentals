import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datasets"

DATA_DIR.mkdir(exist_ok=True)

FILE_PATH = DATA_DIR / "student_performance.csv"

students = [
    ["Yashraj", 92, 88, 95],
    ["Priya", 98, 95, 96],
    ["Rahul", 75, 80, 70],
    ["Neha", 85, 90, 88],
    ["Aman", 70, 72, 75]
]

# Create CSV dataset
with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Name", "Python", "SQL", "MachineLearning"]
    )

    writer.writerows(students)

student_results = []

# Read and process dataset
with open(FILE_PATH, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        python_marks = int(row["Python"])
        sql_marks = int(row["SQL"])
        ml_marks = int(row["MachineLearning"])

        total = (
            python_marks
            + sql_marks
            + ml_marks
        )

        average = total / 3

        student_results.append({
            "name": row["Name"],
            "total": total,
            "average": average
        })

# Calculate statistics
class_average = sum(
    student["average"]
    for student in student_results
) / len(student_results)

topper = max(
    student_results,
    key=lambda student: student["average"]
)

print("=" * 75)
print("              STUDENT PERFORMANCE ANALYZER")
print("=" * 75)

print("\nStudent Results")
print("-" * 75)

for student in student_results:

    print(
        f"{student['name']:10} | "
        f"Total: {student['total']:3} | "
        f"Average: {student['average']:.2f}"
    )

print("-" * 75)

print(f"Class Average : {class_average:.2f}")
print(f"Top Performer : {topper['name']}")
print(f"Top Average   : {topper['average']:.2f}")

print(f"\nDataset saved at: {FILE_PATH}")
print("=" * 75)