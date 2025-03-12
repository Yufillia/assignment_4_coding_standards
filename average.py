# Calculate the Average
numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-numeric to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when user enters an invalid input

if numbers:
    avg = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {avg:.2f}")
else:
    print("No valid numbers entered.")