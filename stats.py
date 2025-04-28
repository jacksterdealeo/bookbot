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

def sort_char_dict(char_dict):
    list_of_char_dict = []
    for key, value in char_dict.items():
        list_of_char_dict.append({"char": key, "num": value})

    # return list_of_char_dict

    def sort_on(dict):
        return dict["num"]
    list_of_char_dict.sort(reverse=True, key=lambda dict: dict["num"])
    return list_of_char_dict

