full_name = input("Please enter your full name in capital letters: ")

def manual_lower_case(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

lower_case_name = manual_lower_case(full_name)
print("Your name in lowercase is: ", lower_case_name)