def manual_endswith(text,suffix):
    if len(suffix) > len(text):
        return False

    n = len(suffix)

    end_part = text[-n:]

    if end_part == suffix:
        return True
    else:
        return False 