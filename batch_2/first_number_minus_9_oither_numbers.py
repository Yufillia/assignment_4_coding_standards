# First Number Minus All the Other 9 Numbers
first_num = int(input("Enter the first number: "))
total = first_num

for _ in range(9):
    num = int(input("Enter a number: "))
    total -= num  # Subtract each entered number from total

print("Result:", total)