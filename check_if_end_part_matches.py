def manual_endswith(text,suffix):
    if len(suffix) > len(text):
        return False

    n = len(suffix)