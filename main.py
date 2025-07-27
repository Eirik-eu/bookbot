from stats import count_words, count_characters, sort_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    print_report(book_path, num_words, num_chars)
    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
    
def print_report(book_path, num_words, num_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # for loop to only print alphanumerical characters
    for item in sort_list(num_chars):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()