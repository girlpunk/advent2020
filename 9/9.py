import itertools
import collections

def load_numbers(file):
    return [int(line) for line in open(file)]


def first(numbers):
    for line in range(25, len(numbers) - 25):
        try:
            next(pair for pair in itertools.combinations(numbers[line - 25:line], 2) if sum(pair) == numbers[line])
        except StopIteration:
            return numbers[line]


def window(sequence, length):
    it = iter(sequence)
    win = collections.deque((next(it, None) for _ in range(length)), maxlen=length)
    yield win
    append = win.append
    for elem in it:
        append(elem)
        yield list(win)


def second(numbers, target):
    for length in range(2, len(numbers)):
        for values in window(numbers, length):
            if sum(values) == target:
                return min(values) + max(values)


def main(file="input.txt"):
    numbers = load_numbers(file)
    one = first(numbers)
    return one, second(numbers, one)


if __name__ == '__main__':
    one, two = main()
    assert one == 530627549
    assert two == 77730285
    print(one)
    print(two)
