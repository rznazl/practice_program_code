history = []
print("Enter multiple numbers. Enter any letter to stop.")

while True:
    user_input = input("Enter a number: ")
    try:
        current_num = int(user_input)

        if current_num in history:
            print("Duplicate")
        else:
            print("Unique")
            history.append(current_num)

    except ValueError:
        print("\nInvalid input detected. Program stops.")
        break