import unittest
import itertools

import random


class CombTestClass(unittest.TestCase):

    # permutations, combinations, product, cycle, chain, islice, range, count,
    # random, repeat, tee, takewhile, ziplongest

    def test_count(self):
        numbers = itertools.islice(itertools.count(), 3)
        assert list(numbers) == list(range(3))

    def test_permutations_combinations(self):
        perms = itertools.permutations(range(3), 2)
        print('perms: ')
        print(list(perms))
        # [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

        combs = itertools.combinations(range(3), 2)
        print('combs: ')
        print(list(combs))
        # [(0, 1), (0, 2), (1, 2)]

        combs_repl = itertools.combinations_with_replacement(range(3), 2)
        print('combs with repl: ')
        print(list(combs_repl))
        # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

        # test that permutations and combinations_with_replacement contain combinations
        for c in combs:
            assert c in perms
            assert c in combs_repl

    def test_product(self):
        pr1 = [(x, y) for x in 'ABC' for y in range(3)]
        pr2 = itertools.product('ABC', range(3))
        assert pr1 == list(pr2)

    def test_chain_cycle(self):
        numbers_twice_1 = itertools.chain(range(3), range(3))
        # [0, 1, 2, 0, 1, 2]
        numbers_twice_2 = itertools.islice(itertools.cycle([0, 1, 2]), 6)
        # [0, 1, 2, 0, 1, 2]
        assert list(numbers_twice_1) == list(numbers_twice_2)

    def random_combination(self, iterable, r):
        "Random selection from itertools.combinations(iterable, r)"
        pool = tuple(iterable)
        n = len(pool)
        indices = sorted(random.sample(range(n), r))
        return tuple(pool[i] for i in indices)

    def test_repeat(self):
        ones = itertools.repeat(1, 5)
        zeros = itertools.repeat(0, 5)

        ones_and_zeros = itertools.chain(ones, zeros)
        assert list(ones_and_zeros) == [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

    def test_compress(self):

        ten_numbers = range(10)
        mods_2 = [num%2 for num in ten_numbers]

        even = itertools.compress(ten_numbers, mods_2)

        assert list(even) == [1, 3, 5, 7, 9]

    def test_tee(self):
        d = itertools.tee(range(10), 2)

        assert len(d) == 2

        for iterator in d:
            for elem in iterator:
                print(elem)
            print('.')

        assert 1 == 1

    def test_ziplongest(self):
        assert list(itertools.zip_longest('AB', 'xyz', fillvalue='-')) == [('A', 'x'), ('B', 'y'), ('-', 'z')]

    def test_takewhile(self):
        assert list(itertools.takewhile(lambda x: x<5, [1,4,6,4,1])) == [1, 4]
