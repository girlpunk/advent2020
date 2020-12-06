def load_seats(file):
    seat_codes = [line.strip() for line in open(file)]

    for seat in seat_codes:
        yield int("".join(["1" if char in ["B", "R"] else "0" for char in seat]), 2)


def first(seats):
    return max(seats)


def second(seats):
    possible_seats = set()

    for seat in seats:
        possible_seats.add(seat+1)
        possible_seats.add(seat-1)

    possible_seats = list(possible_seats - seats)
    possible_seats.sort()

    return possible_seats[1]




def main(file="input.txt"):
    seats = set(load_seats(file))
    return first(seats), second(seats)



def test_jm_5(benchmark):
    one, two = benchmark(main, file="5/input.txt")
    assert one == 930
    assert two == 515



if __name__ == '__main__':
    one, two = main()
    assert one == 930
    assert two == 515
    print(one)
    print(two)
