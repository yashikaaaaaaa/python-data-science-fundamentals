print("=" * 50)
print("      MULTIPLICATION TABLE GENERATOR")
print("=" * 50)

number = int(input("Enter a Number: "))

print()

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")