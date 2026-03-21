numbers = []
duplicates = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}:"))

    if num in numbers and num not in duplicates:
        duplicates.append(num)

        numbers.append(num)

if duplicates:
    print("Numbers with duplicates:", duplicates)
else:
    print("No duplicates found.")