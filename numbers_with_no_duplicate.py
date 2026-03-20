numbers = []
count = 1
while count <= 10:
    val = int(input(f"Enter number {count}: "))
    numbers.append(val)
    count += 1
print("\nNumbers that don't have duplicates: " )

for n in numbers:
    if numbers.count(n) == 1:
        print(n)