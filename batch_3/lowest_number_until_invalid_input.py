# Finds lowest number until invalid input
numbers = []
while True:
    try:
        num = int(input("Enter a number (input a non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when invalid input is entered

if numbers:
    print("Lowest number:", min(numbers))
else:
    print("No numbers were entered.")