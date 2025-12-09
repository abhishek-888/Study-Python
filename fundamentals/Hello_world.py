# This program says hello and asks for my name.

print("Hello, world!")
print("What is your name?")  # Ask for their name.
my_name = input("Your name is : ")
print("It is good to meet you, " + my_name)
print("The length of your name is:")
print(len(my_name))
print("What is your age?")  # Ask for their age.
my_age = input("Your age is : ")
print("You will be " + str(int(my_age) + 1) + " in a year.")
