any_statement = "programming"
target_letter = "m"

any_statement_length = len(any_statement)
target_letter_length = len(target_letter)
count = 0

for i in range (any_statement_length- target_letter_length + 1):
    window = any_statement[i: i + target_letter_length]
    