numbers = []

print("Enter numbers one by one. Enter any letter to stop.")

while True:
    user_input = input("Enter a number: ")

    try:
        current_num = float(user_input)
        numbers.append(current_num)
    except ValueError:
        break

if not numbers:
    print("No numbers were detected.")
else:
    most_frequent = numbers[0]
    max_count = 0

    for n in set(numbers):
        current_count = numbers.count(n)

        if current_count > max_count:
            max_count = current_count
            most_frequent = n

    if max_count > 1:
        prin(f"The number with the most duplicates is {most_frequent}.")
        print(f"It appeared {max_count} times.")
    else:
        print("All the numbers are unique and there are no duplicates found.")