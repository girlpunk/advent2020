def load_seats():
    seat_codes = open("input.txt")

    for seat in seat_codes:
        yield int(seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)


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


if __name__ == '__main__':
    seats = set(load_seats())
    print(first(seats))
    print(second(seats))
