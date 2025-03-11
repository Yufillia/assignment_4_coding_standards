# Count Odd numbers in 10 inputs
count = 0
for _ in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        count += 1
print("Odd numbers count:", count)