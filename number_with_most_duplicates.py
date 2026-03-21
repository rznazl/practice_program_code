numbers = []

print("Enter numbers one by one. Enter any letter to stop.")

while True:
    user_input = input("Enter a number: ")

    try:
        current_num = float(user_input)
        numbers.append(current_num)
    except ValueError:
        break