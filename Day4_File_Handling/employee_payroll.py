import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datasets"

DATA_DIR.mkdir(exist_ok=True)

FILE_PATH = DATA_DIR / "employees.csv"

employees = [
    ["Aman", "IT", 65000],
    ["Priya", "HR", 55000],
    ["Rahul", "Finance", 72000],
    ["Neha", "IT", 80000],
    ["Arjun", "Marketing", 60000]
]

# Create employee CSV
with open(FILE_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Department", "Salary"])
    writer.writerows(employees)

total_salary = 0
highest_salary = 0
highest_paid = ""

# Read and analyze employee data
with open(FILE_PATH, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for employee in reader:

        salary = float(employee["Salary"])

        total_salary += salary

        if salary > highest_salary:
            highest_salary = salary
            highest_paid = employee["Name"]

employee_count = len(employees)
average_salary = total_salary / employee_count

print("=" * 65)
print("               EMPLOYEE PAYROLL ANALYZER")
print("=" * 65)

print(f"\nTotal Employees : {employee_count}")
print(f"Total Payroll   : ₹{total_salary:,.2f}")
print(f"Average Salary  : ₹{average_salary:,.2f}")
print(f"Highest Paid    : {highest_paid}")
print(f"Highest Salary  : ₹{highest_salary:,.2f}")

print("\nEmployee Records")
print("-" * 65)

with open(FILE_PATH, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for employee in reader:
        print(
            f"{employee['Name']:10} | "
            f"{employee['Department']:12} | "
            f"₹{float(employee['Salary']):,.2f}"
        )

print("-" * 65)
print(f"File saved at: {FILE_PATH}")
print("=" * 65)