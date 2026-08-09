print("=" * 50)
print("         WELCOME TO PYTHON BANK")
print("=" * 50)

balance = 50000

pin = input("Enter your 4-digit PIN: ")

if pin == "1234":

    print("\nLogin Successful")

    print("""
1. Check Balance
2. Deposit Money
3. Withdraw Money
""")

    choice = int(input("Choose Option: "))

    if choice == 1:
        print(f"Available Balance : ₹{balance}")

    elif choice == 2:
        amount = float(input("Deposit Amount: ₹"))
        balance += amount
        print(f"Updated Balance : ₹{balance}")

    elif choice == 3:
        amount = float(input("Withdraw Amount: ₹"))

        if amount <= balance:
            balance -= amount
            print(f"Please collect your cash.")
            print(f"Remaining Balance : ₹{balance}")
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Choice")

else:
    print("Incorrect PIN")