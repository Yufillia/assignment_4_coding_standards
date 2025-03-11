# Display All Numbers (gnoring Duplicate Entries After the First One
numbers = []
seen = set()

print("Enter 10 numbers:")
for _ in range(10):
    num = int(input())
    if num not in seen:
        numbers.append(num)
        seen.add(num)

print("Numbers (only first occurrence of duplicates shown):", numbers)
