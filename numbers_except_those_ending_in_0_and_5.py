# Print Numbers 0 to 100 Except Those Ending in 0 or 5
for i in range(101):
    if i % 10 != 0 and i % 10 != 5:  # Exclude numbers ending in 0 or 5
        print(i)