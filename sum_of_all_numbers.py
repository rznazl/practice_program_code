total_sum = 0
count = 1

while count <= 10:
    num = float(input(f"Enter number {count}: "))
    total_sum += num
    count += 1

print(f"The sum of all 10 numbers is {total_sum}")
