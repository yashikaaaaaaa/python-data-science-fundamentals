age = int(input("Enter Age: "))
day = input("Enter Day (Weekday/Weekend): ").lower()

if age < 5:
    ticket = 0

elif age <= 18:

    if day == "weekday":
        ticket = 120
    else:
        ticket = 180

elif age <= 60:

    if day == "weekday":
        ticket = 250
    else:
        ticket = 350

else:

    ticket = 150

print(f"Ticket Price : ₹{ticket}")