def two():
    """Find two numbers from the input list that sum to 2020, and calculate the product"""
    numbers = [int(line) for line in open("input.txt")]

    for a in numbers:
        for b in numbers:
            if a == b:
                continue
            if a + b == 2020:
                print(f"Found two numbers: {a}, {b}")
                print(f"Sum: {a*b}")
                return


def three():
    """Find three numbers from the input list that sum to 2020, and calculate the product"""
    numbers = [int(line) for line in open("input.txt")]

    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a == b or b == c or a == c:
                    continue
                if a + b + c == 2020:
                    print(f"Found three numbers: {a}, {b}, {c}")
                    print(f"Sum: {a*b*c}")
                    return


if __name__ == '__main__':
    two()
    three()
