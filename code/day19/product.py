from itertools import product

string = "Tafsir"
for letter in product(string, repeat=1):
    print(letter)
# ('T',)
# ('a',)
# ('f',)
# ('s',)
# ('i',)
# ('r',)

for letter in product(string, repeat=2):
    print(letter)
# ('T', 'T')
# ('T', 'a')
# ('T', 'f')
# ('T', 's')
# ('T', 'i')
# ('T', 'r')
# ('a', 'T')
# ('a', 'a')
# ('a', 'f')
# ('a', 's')
# ('a', 'i')
# ('a', 'r')
# ('f', 'T')
# ('f', 'a')
# ('f', 'f')
# ('f', 's')
# ('f', 'i')
# ('f', 'r')
# ('s', 'T')
# ('s', 'a')
# ('s', 'f')
# ('s', 's')
# ('s', 'i')
# ('s', 'r')
# ('i', 'T')
# ('i', 'a')
# ('i', 'f')
# ('i', 's')
# ('i', 'i')
# ('i', 'r')
# ('r', 'T')
# ('r', 'a')
# ('r', 'f')
# ('r', 's')
# ('r', 'i')
# ('r', 'r')
