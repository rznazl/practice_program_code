lowest = None

print("Enter any number. Enter any letter to stop the program.")

while True:
    user_input = input("Enter a number: ")

    try:
        current_num = int(user_input)

        if lowest is None or current_num < lowest:
            lowest = current_num

    except valueError:
        print("\nInvalid input detected. The program will now stop.")
        break 