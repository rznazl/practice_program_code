statement = "I love my life"
prefix = "I"

if text.startswith(prefix):
    result = text[len(prefix):]
else:
    result = statement
    