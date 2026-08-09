import csv
import os

# Create the datasets folder automatically
os.makedirs("Day4_File_Handling/datasets", exist_ok=True)

file_name = "Day4_File_Handling/datasets/students.csv"

students = [
    ["Yashraj", "Data Science", 8.7],
    ["Priya", "Computer Science", 9.2],
    ["Rahul", "Data Science", 7.9],
    ["Neha", "AI", 8.9]
]

# Write data to CSV
with open(file_name, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Department", "CGPA"])
    writer.writerows(students)

print("Student records saved successfully.")

# Read data from CSV
with open(file_name, "r") as file:
    reader = csv.DictReader(file)

    print("\nStudent Records")
    print("-" * 55)

    for row in reader:
        print(
            f"{row['Name']:10} | "
            f"{row['Department']:18} | "
            f"CGPA: {row['CGPA']}"
        )

print("-" * 55)