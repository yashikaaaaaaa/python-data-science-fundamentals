employees = int(input("Number of Employees: "))

print()

for i in range(employees):

    print(f"Employee {i+1}")

    name = input("Name : ")

    basic = float(input("Basic Salary : ₹"))

    hra = basic * 0.20
    da = basic * 0.10
    tax = basic * 0.05

    net = basic + hra + da - tax

    print("-" * 40)
    print(f"Employee : {name}")
    print(f"Net Salary : ₹{net:.2f}")
    print("-" * 40)