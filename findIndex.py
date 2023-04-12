# Functie ie ik gebruikt heb om de positie van ul te vinden in de html

with open("index.html", "r") as html_logger:
    html_text = html_logger.read()


def find_character_index(string, char):
    if char in string:
        index = string.index(char)
        negative_index = len(string) - index
        return index, negative_index
    else:
        return -1, -1


index, negative_index = find_character_index(html_text, "?")
print(index)
print(negative_index)
