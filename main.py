from stats import count_words, count_chars, sort_char_data
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    contents_string = get_book_text(book_path)
    num_words = count_words(contents_string)
    num_chars = count_chars(contents_string)
    chars = sort_char_data(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
