sample_text = "I love my life"
given_suffix = "life"

if given_suffix and sample_text.endswith (given_suffix):
    result = sample_text[:-len(given_suffix)]
else:
    result = sample_text

print("Statement without suffix: ", result)