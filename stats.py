def get_num_words(book):
    word_array = book.split()
    num_words = len(word_array)
    return num_words

def sort_on(items):
    return items["num"]

def set_recurring_dictionary(counts):
    new_dict_list = []
    for char, count in counts.items():
        new_dict_list.append({"char": char, "num": count})
    return new_dict_list

def get_recurring_characters(book):
    char_dict = {}
    characters = [char.lower() for char in book]
    for char in characters:
        char_dict[char] = char_dict.get(char, 0) + 1
    lst = set_recurring_dictionary(char_dict)
    lst.sort(reverse=True, key=sort_on)
    return lst