def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


def main():
    try:
        number = int(input("Enter a number: "))
        while number != 1:
            number = collatz(number)
            print(str(number) + "", end=" ")
    except ValueError:
        print("Invalid input. Please enter an integer.")


main()
