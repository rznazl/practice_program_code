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