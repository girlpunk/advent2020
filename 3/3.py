
from functools import reduce
import math

Tree = '#'


def load_file(file):
    file = [line.strip() for line in open(file)]
    line_length = len(file[0])
    return file, line_length


def first(file, line_length, across=3, down=1):
    current_across = across
    current_down = down
    trees = 0
    file_len = len(file)

    while current_down + 1 <= file_len:
        if file[current_down][current_across] == Tree:
            trees += 1

        current_across = (current_across + across) % line_length
        current_down += down

    return trees


def second(file, line_length):
    pairs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    results = [first(file, line_length, across, down) for across, down in pairs]

    result = reduce((lambda x, y: x * y), results)

    return result


def main(file="input.txt"):
    content, line_length = load_file(file)
    return first(content, line_length), \
        second(content, line_length)



def test_jm_3(benchmark):
    one, two = benchmark(main, file="3/input.txt")
    assert one == 286
    assert two == 3638606400
    print(one)
    print(two)


if __name__ == '__main__':
    one, two = main()
    assert one == 286
    assert two == 3638606400
    print(one)
    print(two)
