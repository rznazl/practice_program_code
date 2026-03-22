numbers = []

print("Enter any number. Enter any letter to stop the program.")

while True:
    user_input = input("Enter here: ")
    try:
        num = int(user_input)
        number.append(num)
    except ValueError:
        break
        