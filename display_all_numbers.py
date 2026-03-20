all_numbers = []
seen_numbers = []
count = 1
while count <= 10:
    val = int(input(f"Enter number {count}: "))
    all_numbers.append(val)
    count += 1
print("\nDisplaying all numbers (numbers with duplicates are only shown once):")
for n in all_numbers:
    if n not in seen_numbers:
        print(n)
        seen_numbers.append(n)