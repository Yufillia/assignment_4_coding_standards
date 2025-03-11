# Sort Numbers from Lowest to Highest Until Invalid Input
numbers = []
while True:
    try:
        num = int(input("Enter a number (or non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when invalid input is entered