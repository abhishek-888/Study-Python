cats = []

while True:
    print("Enter the name of cat" + str(len(cats) + 1) + "(Or enter nothing to stop.)")
    name = input()
    if name == "":
        break
    cats.append(name)

print("The list of cats is:")
for i, cat in enumerate(cats):
    print("Your no. " + str(i + 1) + " cat is " + cat)
