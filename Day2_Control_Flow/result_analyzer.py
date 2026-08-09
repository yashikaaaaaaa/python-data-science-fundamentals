print("=" * 60)
print("          STUDENT RESULT ANALYZER")
print("=" * 60)

students = int(input("Enter Number of Students: "))

highest = 0
topper = ""

for i in range(students):

    print(f"\nStudent {i+1}")

    name = input("Name : ")
    marks = float(input("Marks : "))

    if marks > highest:
        highest = marks
        topper = name

print("\n" + "=" * 60)
print(f"Top Performer : {topper}")
print(f"Highest Marks : {highest}")
print("=" * 60)