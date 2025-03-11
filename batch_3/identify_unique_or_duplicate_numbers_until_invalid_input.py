# Identify Unique or Duplicate Numbers Until Invalid Input
numbers = []
while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        if num in numbers:
            print("Duplicate", numbers)  # Show list for debugging
        else:
            print("Unique", numbers)  # Show list for debugging
            numbers.append(num)
    except ValueError:  # Stops when the user enters an invalid input
        break