# Display numbers without duplicates
numbers = []
unique_numbers = []

print("Enter 10 numbers:")
for _ in range(10):
    num = int(input())
    numbers.append(num)

for num in numbers:
    if numbers.count(num) == 1:  # If the number appears only once, it's unique
        unique_numbers.append(num)

print("Numbers without duplicates:", unique_numbers)
