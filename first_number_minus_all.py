#input the first number
total = float(input("Enter number 1: "))
#loop 9 times to get the remaining numbers
count = 2
while count <= 10:
    num = float(input(f"Enter number {count}: "))
#subtract the numbers
    total -= num
    count += 1
#print the final result
print(f"The result is: {total}")