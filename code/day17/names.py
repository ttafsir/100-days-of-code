import random


NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]

# convert these names to title case (brad pitt -> Brad Pitt)
names = [name.title() for name in NAMES]


def reverse_first_last_names():
    return [
        f"{last} {first}"
        for first, last in (name.split() for name in names)
    ]


def gen_pairs():
    first_names = [name.split()[0] for name in names]
    while True:
        rand_a, rand_b = random.sample(first_names, 2)
        if rand_a == rand_b:
            continue
        yield f'{rand_a} teams up with {rand_b}'


print(reverse_first_last_names())
print()

# use this same list and make a little generator
pairs = gen_pairs()
for _ in range(10):
    print(next(pairs, None))
print()

# Another way to get a slice of a generator is using itertools.islice:
import itertools  # noqa
first_ten = itertools.islice(pairs, 10)
print(list(first_ten))
