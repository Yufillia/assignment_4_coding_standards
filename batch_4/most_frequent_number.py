# Find the Most Frequent Number
numbers = []

while True:
    try:
        num = int(input("Enter a number (or non-numeric to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when user enters an invalid input

if numbers:
    # Manually count occurrences
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # Find the highest occurrence count
    max_count = max(frequency.values())

    # If all numbers appear only once, there's no most frequent number
    if max_count == 1:
        print("No frequent number (all numbers are unique).")
    else:
        # Find the number(s) that appeared the most times
        most_frequent = [num for num, count in frequency.items() if count == max_count]
        print(f"The most frequent number(s): {most_frequent} (appeared {max_count} times).")
else:
    print("No numbers entered.")
