
def manual_rindex(text, target):
    for i in range(len(text) - 1, -1, -1):
        if text[i] == target:
            return i
    raise ValueError("Target not found.")

sample_string = "banana"
char = "a"
print(f"The last location of '{char}' is: {manual_rindex(string, char)}")
