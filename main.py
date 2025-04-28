from stats import word_count
from stats import char_count

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    print(word_count(text), "words found in the document")
    count = char_count(text)
    print(count)

main()

