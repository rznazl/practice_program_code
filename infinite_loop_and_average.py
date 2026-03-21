numbers: []
while True:
    value = input("Enter any number. Enter any letter to stop: ")
    try:
        nums.append(int(value))
    except ValueError:
        break