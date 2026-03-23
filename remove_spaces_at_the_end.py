any_statement = input("Enter any string and add spaces at the end: ")

index = len(any_statement) - 1

while index >= 0 and any_statement[index] != " ":
    index -= 1