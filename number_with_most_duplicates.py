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
