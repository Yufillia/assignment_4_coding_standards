# Even numbers in 10 inputs
count = 0
for _ in range(10):
    num = int(input("Enter a number: "))
    if num % 2 == 0:  # Check if even
        count += 1
print("Even numbers count:", count)