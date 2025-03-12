# Find the Most Frequent Number

numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-numeric to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when user enters an invalid input

if numbers:
    # Manually count occurrences instead of using Counter
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # Find the number with the highest occurrence
    most_frequent = max(frequency, key=frequency.get)
    print(f"The number {most_frequent} appeared the most times ({frequency[most_frequent]} times).")
else:
    print("No numbers entered.")
