any_statement = input("Enter any text: ")
target_length = int(input("Enter your target length: "))

padding_size = target_length - len(any_statement)

if padding_size > 0:
    result = ("0" * padding_size) + any_statement
else:
    result = any_statement
    
print(f"Output: {result}")