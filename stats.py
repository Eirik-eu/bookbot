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

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_list(dict):
    sorted_list = []
    for item in dict:
        sorted_list.append({"char": item, "num": dict[item]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    