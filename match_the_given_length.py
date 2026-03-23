example_string = "Love"
given_length = 10

padding_size = given_length -len(example_string)

if padding_size > 0:
    result = example_string + (" " * padding_size)
else:
    result = example_string

print(f"Output: '{result}'")
print(f"The total length is: {len(result)}")