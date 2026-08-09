cgpa = float(input("CGPA : "))
income = float(input("Annual Family Income : "))

if cgpa >= 9.0 and income <= 300000:
    print("100% Scholarship")

elif cgpa >= 8.0 and income <= 500000:
    print("50% Scholarship")

elif cgpa >= 7.0:
    print("25% Scholarship")

else:
    print("Scholarship Not Eligible")