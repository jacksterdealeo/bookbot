def word_count(text):
    return (len(text.split()))

def char_count(text):
    # might edit the original text?
    # not sure if it's a copy or ref.
    text = text.lower()
    char_dict = {}
    for c in text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

