list_of_vowels =["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]


def vowel_counter(string):
    counter = 0
    for letter in string:
        if letter in list_of_vowels:
            counter += 1
    return counter
