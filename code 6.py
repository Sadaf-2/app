try:
    num = int(input("Enter a number: "))
    print("Square is:", num ** 2)
except ValueError:
    print("Invalid input. Please enter a number.")
