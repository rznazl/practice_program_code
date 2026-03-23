any_statement = input("Enter any text: ")

is_all_lower = True
found_letter = False

for char in any_statement:
    if 'A' <= char <= 'Z':
        is_all_lower = False
        break
    if 'a' <= char <= 'z':
        found_letter = True
        