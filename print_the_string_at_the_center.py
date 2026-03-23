sample_string = "Programming"
given_length = 20

total_padding = given_length - len(sample_string)

left_padding = total_padding // 2
right_padding = total_padding - left_padding

if given_length > len(sample_string):
    result = (" " * left_padding) + sample_string + (" " * right_padding)
else:
    result = text

print(f"Output: '{result}'")
print(f"Total length: {len(result)}")