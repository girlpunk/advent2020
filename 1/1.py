import itertools

def two(numbers):
    """Find two numbers from the input list that sum to 2020, and calculate the product"""
    for pair in itertools.combinations(numbers, 2):
        if sum(pair) == 2020:
            return pair[0]*pair[1]

def three(numbers):
    """Find three numbers from the input list that sum to 2020, and calculate the product"""

    for pair in itertools.combinations(numbers, 3):
        if sum(pair) == 2020:
            return pair[0]*pair[1]*pair[2]


def main(file="input.txt"):
    numbers = [int(line) for line in open(file)]
    return two(numbers), three(numbers)


def test_jm_1(benchmark):
    one, two = benchmark(main, file="1/input.txt")
    assert one == 365619
    assert two == 236873508


if __name__ == '__main__':
    one, two = main()
    assert one == 365619
    assert two == 236873508
    print(one)
    print(two)
