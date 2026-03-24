sample_text = "Python Programming"
target_to_find = "gram"

sample_text_length = len(sample_text)
target_to_find_length = len(target_to_find)
found_index = -1

for i in range(sample_text_length - target_to_find_length + 1):
    if sample_text[i : i + target_to_find_length] == target:
        found_index = i
        break

if found_index != 1:
    print(f"The target '{target_to_find}' starts at index :{found_index}")
else:
    print("Target found.")