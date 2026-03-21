highest = None

while True:
    user_input = input("Enter any number. Enter any letter to stop.")

    try:
        num = int(user_input)

        if highest is None or num > highest:
            highest = num 