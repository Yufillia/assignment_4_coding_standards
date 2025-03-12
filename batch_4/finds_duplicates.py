numbers = []
duplicates = set()

print("Enter 10 numbers:")

for _ in range(10):
    num = int(input("Enter a number: "))
    
    # Check if the number already exists in the list
    if num in numbers and num not in duplicates:
        duplicates.add(num)
    
    numbers.append(num)

# Display the duplicates if found, otherwise say none were found
if duplicates:
    print("Duplicate numbers:", list(duplicates))
else:
    print("No duplicate numbers found.")