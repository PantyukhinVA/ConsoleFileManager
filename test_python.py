import math
import random


def test_pi():
    assert(math.pi == 3.141592653589793)


def test_sorted():
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_arr = random.sample(sorted_arr, len(sorted_arr))

    assert(sorted(random_arr) == sorted_arr)


def test_filter():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert([1, 2, 3] == list(filter(lambda a: a <= 3, arr)))


def test_sqrt():
    assert(math.sqrt(9) == 3)


def test_map():
    arr = [1, 2, 3, 4, 5]

    assert(list(map(lambda a: a ** 2, arr)) == [1 ** 2, 2 ** 2, 3 ** 2, 4 ** 2, 5 ** 2])


def test_pow():
    assert(math.pow(5, 2) == 25)


def test_hypot():
    x = 10
    y = 5

    assert(math.hypot(10, 5) == math.sqrt(x * x + y * y))
