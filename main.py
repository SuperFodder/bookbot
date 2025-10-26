from stats import get_num_words
from stats import get_recurring_characters

def get_book_text(path_str):
    with open(path_str) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    dict_list = get_recurring_characters(book_text)
    for item in dict_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

main()