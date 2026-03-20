odd_count = 0

print("Please enter 10 numbers")

for i in range (1,11):
    number = int(input(f"Enter number {i}: "))
    if number % 2 != 0:
        odd_count += 1
print(f"The total od the odd numbers is {odd_count}.")