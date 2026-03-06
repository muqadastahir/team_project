users = {
    "user1": "pass123",
    "user2": "mypassword"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed! Check username and password.")