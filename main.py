#!/usr/bin/env python3
import sys

from stats import word_count
from stats import char_count
from stats import sort_char_dict

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_location = sys.argv[1]
    text = get_book_text(book_location)
    print(word_count(text), "words found in the document")
    count = char_count(text)
    char_dict_list = sort_char_dict(count)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_location}...
----------- Word Count ----------
Found {word_count(text)} total words
--------- Character Count -------""")

    for char_dict in char_dict_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")

main()

