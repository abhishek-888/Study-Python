username = input("Your name is : ")
password = input("Your password is : ")
if username == "kikki":
    print("Welcome, kikki!")
    if password == "1234":
        print("Access granted!")
    elif password == "12345":
        print("Root Access granted!")
    else:
        print("Access denied!")
else:
    print("Hello Stranger!")
