# Print All Numbers Between Two Given Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Ensure num1 is smaller
if num1 > num2:
    num1, num2 = num2, num1  

for i in range(num1 + 1, num2):  # Print numbers between num1 and num2
    print(i)