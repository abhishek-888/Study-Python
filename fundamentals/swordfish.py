while True:
    print("Who are you?")
    name = input(">")
    if name != "Joe" and name != "joe":
        continue
    print("Hello,Joe.What is the password?")
    password = input("Password:")
    if password == "swordfish":
        break
    else:
        print("wrong password, You are not Joe.")
print("Access granted.")
