def count_words(contents):
    words_list = contents.split()
    return len(words_list)


def count_chars(contents):
    char_count = {}
    for character in contents:
        character = character.lower()
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count


def sort_char_data(char_data):
    result = []

    def sort_on(items):
        return items["num"]

    for key, value in char_data.items():
        new_dict = {"char": key, "num": value}
        result.append(new_dict)

    result.sort(reverse=True, key=sort_on)

    return result
