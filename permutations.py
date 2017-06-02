import itertools

l = range(1, 6)
for elem in itertools.permutations(l, 2):
    print(elem)
