import sys
import functools

def load_adapters(file):
    return [int(line) for line in open(file)]


def first(adapters):
    current = 0
    ones = 0
    threes = 1
    adapters.sort()
    for adapter in adapters:
        if adapter - 1 == current:
            ones += 1
        elif adapter - 2 == current:
            pass
        elif adapter - 3 == current:
            threes += 1
        else:
            print("Unknown adapter distance!")
        current = adapter
    return ones * threes

@functools.lru_cache(maxsize=sys.maxsize)
def second_recurse(adapters: tuple, start: int, end: int):
    next_adapters = [adapter for adapter in adapters if adapter-3 <= start]
    return sum([True for adapter in next_adapters if adapter + 3 >= end]) +\
           sum([second_recurse(tuple(next_adapter for next_adapter in adapters if next_adapter > adapter), adapter, end) for adapter in next_adapters])


def second(adapters):
    end = max(adapters)+3
    return second_recurse(tuple(adapters), 0, end)


def main(file="input.txt"):
    adapters = load_adapters(file)
    return first(adapters), second(adapters)


if __name__ == '__main__':
    one, two = main()
    assert one == 1656
    assert two == 56693912375296
    print(one)
    print(two)
