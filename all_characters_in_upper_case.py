full_name = input("Enter your full name: ")
upper_case_name = ""

for char in full_name:
    ascii_val = ord(char)

    if 97 <= ascii_val <= 122:
        upper_case_name += chr(ascii_val - 32)
    else:
        upper_case_name += char

print("Full name in uppercase: ", upper_case_name)