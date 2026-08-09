employees = [
    {"name": "Aman", "department": "IT", "salary": 65000},
    {"name": "Priya", "department": "HR", "salary": 55000},
    {"name": "Rahul", "department": "Finance", "salary": 72000},
    {"name": "Neha", "department": "IT", "salary": 80000},
    {"name": "Arjun", "department": "Marketing", "salary": 60000}
]

print("=" * 60)
print("               EMPLOYEE SALARY ANALYZER")
print("=" * 60)

for employee in employees:
    print(
        f"{employee['name']:10} | "
        f"{employee['department']:10} | "
        f"₹{employee['salary']:,}"
    )

highest_paid = max(employees, key=lambda employee: employee["salary"])

average_salary = sum(
    employee["salary"] for employee in employees
) / len(employees)

it_employees = [
    employee["name"]
    for employee in employees
    if employee["department"] == "IT"
]

print("\n" + "-" * 60)
print(f"Highest Paid Employee : {highest_paid['name']}")
print(f"Highest Salary        : ₹{highest_paid['salary']:,}")
print(f"Average Salary        : ₹{average_salary:,.2f}")
print(f"IT Employees          : {', '.join(it_employees)}")
print("=" * 60)