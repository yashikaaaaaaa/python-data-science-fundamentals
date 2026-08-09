password = input("Create Password : ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for char in password:

    if char.isupper():
        uppercase += 1

    elif char.islower():
        lowercase += 1

    elif char.isdigit():
        digits += 1

    else:
        special += 1

print("\nPassword Analysis")
print("------------------------")
print("Uppercase :", uppercase)
print("Lowercase :", lowercase)
print("Digits    :", digits)
print("Special   :", special)

if (
    len(password) >= 8
    and uppercase >= 1
    and lowercase >= 1
    and digits >= 1
    and special >= 1
):
    print("\nStrong Password ✅")
else:
    print("\nWeak Password ❌")