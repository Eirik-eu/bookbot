from stats import count_words, count_characters, sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text('books/frankenstein.txt')
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    # for loop to only print alphanumerical characters
    for item in sort_list(count_characters(book_text)):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()