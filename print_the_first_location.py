sample_text = "Python Programming"
target_to_find = "gram"

sample_text_length = len(sample_text)
target_to_find_length = len(target_to_find)
found_index = -1

for i in range(sample_text_length - target_to_find_length + 1):
    if text[i : i + target_to_find_length] == target:
        found_index = i
        break