# Highest to Lowest
while True:
    try:
        num = int(input("Enter a number (or non-numeric to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when user enters an invalid input

if numbers:
    numbers.sort(reverse=True)  # Sort descending
    print("Numbers sorted from highest to lowest:", numbers)
else:
    print("No valid numbers entered.")