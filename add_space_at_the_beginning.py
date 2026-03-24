sample_string = "Love"
given_length = 15

padding_size = given_length - len(sample_string)

if padding_size > 0:
    result = (" " * padding_size) + sample_string
else:
    result = sample_string

print(f"Output: {result}")
print(f"Total length: {len(result)}")