database = {
    "admin": "python123",
    "yashraj": "datascience",
    "guest": "guest123"
}

username = input("Username: ")
password = input("Password: ")

if username in database:

    if database[username] == password:
        print("Login Successful")
        print(f"Welcome {username}")

    else:
        print("Incorrect Password")

else:
    print("User Not Found")