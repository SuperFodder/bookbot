from stats import get_num_words
from stats import get_recurring_characters
import sys

def get_book_text(path_str):
    with open(path_str) as f:
        file_contents = f.read()
        return file_contents

def main():
    try: 
        book_text = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count -----------")
        print(f"Found {get_num_words(book_text)} total words")
        print("--------- Character Count -------")
        dict_list = get_recurring_characters(book_text)
        for item in dict_list:
            ch = item["char"]
            if ch.isalpha():
                print(f"{ch}: {item['num']}")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")

main()