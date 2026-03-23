def manual_endswith(text,suffix):
    if len(suffix) > len(text):
        return False

    n = len(suffix)

    end_part = text[-n:]

    if end_part == suffix:
        return True
    else:
        return False

example_statement = input ("Enter any sentence: ")
given_suffix = input ("Enter the word to be check: ")

if manual_endswith(example_statement, given_suffix):
    print(f"Yes, The string ends with '{given_suffix}'.")
else:
    print(f"No, it does not match.")