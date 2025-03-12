# Highest Number
numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-numeric to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when user enters an invalid input

if numbers:
    print("The highest number entered is:", max(numbers))
else:
    print("No valid numbers entered.")