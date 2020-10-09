from random import *


class letter():
    # Each letter has a lowercase character, an uppercase character, and
    # identifiers as vowel or consonant.
    def __init__(self, lowerchar, upperchar, is_vowel):
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.is_vowel = is_vowel


# Define the alphabet.
global alphabet
alphabet = [letter('a', 'A', True),
            letter('b', 'B', False),
            letter('c', 'C', False),
            letter('d', 'D', False),
            letter('e', 'E', True),
            letter('f', 'F', False),
            letter('g', 'G', False),
            letter('h', 'H', False),
            letter('i', 'I', True),
            letter('j', 'J', False),
            letter('k', 'K', False),
            letter('l', 'L', False),
            letter('m', 'M', False),
            letter('n', 'N', False),
            letter('o', 'O', True),
            letter('p', 'P', False),
            letter('q', 'Q', False),
            letter('r', 'R', False),
            letter('s', 'S', False),
            letter('t', 'T', False),
            letter('u', 'U', True),
            letter('v', 'V', False),
            letter('w', 'W', False),
            letter('x', 'X', False),
            letter('y', 'Y', True),
            letter('y', 'Y', False),
            letter('z', 'Z', False)
            ]


def rand_int(x1, x2):
    # Generate a random integer number between x1 and x2, inclusive.
    r = int(int(x1) + random()*(int(x2)-int(x1)))
    return r


def make_name():
    # Determine name length.
    lmin = 3  # Minimum length.
    lmax = 10  # Maximum length.
    name_length = rand_int(lmin, lmax)

    # Initialize string.
    my_name = ""

    prev_vowel = False  # Was the previous letter a vowel?
    prev_consonant = False  # Was the previous letter a consonant?
    prev2_vowel = False  # Were the previous 2 letters vowels?
    prev2_consonant = False  # Were the previous 2 letters consonants?

    # Generate letters for name.
    for i in range(0, name_length):
        a = get_letter(prev2_vowel, prev2_consonant)
        if (i == 0):
            my_name = my_name + a.upperchar
        else:
            my_name = my_name + a.lowerchar
        prev2_vowel = (a.is_vowel and prev_vowel)
        prev2_consonant = (a.is_vowel is False and prev_consonant)
        prev_vowel = a.is_vowel
        prev_consonant = a.is_vowel is False

    return my_name


def get_letter(need_consonant, need_vowel):
    global alphabet
    # Generate a random letter.
    done = False
    while (not done):
        a = alphabet[rand_int(0, 25)]
        if ((need_consonant and a.is_vowel) or (need_vowel and a.is_vowel is False)):
            done = False
        else:
            done = True
    return a


# Generate and print a name.
name1 = make_name()
print(name1)
