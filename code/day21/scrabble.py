import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])



def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
    valid dictionary words. Use _get_permutations_draw and provided
    dictionary"""
    for p in _get_permutations_draw(draw):
        word = ''.join(p).lower()
        if word in dictionary:
            yield word


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
    use itertools.permutations (order of letters matters)"""
    for length in range(1, 8):
        yield from itertools.permutations(draw, r=length)


if __name__ == "__main__":
    draw = 'G, A, R, Y, T, E, V'.split(", ")

    for p in get_possible_dict_words(draw):
        print(p)
