def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters_dict = {}
    for character in text.lower():
        if character in characters_dict:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1

    return characters_dict