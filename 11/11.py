import numpy

Floor = 0
Occupied = 1
Free = 2


def load_seats(file):
    return numpy.array([[int(char) for char in line.strip().replace('.', str(Floor)).replace('L', str(Free)).replace('#', str(Occupied))] for line in open(file)])


def first(seats):
    xRange = len(seats)
    yRange = len(seats[0])
    while True:
        newSeats = seats.copy()
        changes = 0
        for x in range(0, xRange):
            for y in range(0, yRange):
                if seats[x][y] == Floor:
                    continue
                surrounding = seats[max(x-1, 0):min(x+2, xRange+1), max(y-1, 0):min(y+2, yRange+1)]
                if seats[x][y] == Free:
                    if sum(sum(surrounding == Free)) == sum(sum(surrounding != Floor)):
                        newSeats[x][y] = Occupied
                        changes += 1
                        continue
                if seats[x][y] == Occupied:
                    if sum(sum(surrounding == Occupied)) >= 5:
                        newSeats[x][y] = Free
                        changes += 1
                        continue
        if changes == 0:
            return sum(sum(seats == Occupied))
        seats = newSeats


def second(seats):
    xRange = len(seats)
    yRange = len(seats[0])
    round = 0
    while True:
        round += 1
        newSeats = seats.copy()
        changes = 0
        for x in range(0, xRange):
            for y in range(0, yRange):
                if seats[x][y] == Floor:
                    continue
                surrounding = numpy.array([])

                up_range = seats[0:x, y]
                up = up_range[numpy.nonzero(up_range)]
                if len(up) > 0:
                    surrounding = numpy.append(surrounding, up[-1])

                down_range = seats[x+1:xRange+x, y]
                down = down_range[numpy.nonzero(down_range)]
                if len(down) > 0:
                    surrounding = numpy.append(surrounding, down[0])

                left_range = seats[x, 0:y]
                left = left_range[numpy.nonzero(left_range)]
                if len(left) > 0:
                    surrounding = numpy.append(surrounding, left[-1])

                right_range = seats[x, y+1:yRange+y]
                right = right_range[numpy.nonzero(right_range)]
                if len(right) > 0:
                    surrounding = numpy.append(surrounding, right[0])

                diagonal_check = 1
                while True:
                    if x-diagonal_check < 0 or y-diagonal_check < 0:
                        break
                    check = seats[x-diagonal_check, y-diagonal_check]
                    if check != Floor:
                        surrounding = numpy.append(surrounding, check)
                        break
                    diagonal_check += 1

                diagonal_check = 1
                while True:
                    if x+diagonal_check >= xRange or y+diagonal_check >= yRange:
                        break
                    check = seats[x+diagonal_check, y+diagonal_check]
                    if check != Floor:
                        surrounding = numpy.append(surrounding, check)
                        break
                    diagonal_check += 1

                diagonal_check = 1
                while True:
                    if x+diagonal_check >= xRange or y-diagonal_check < 0:
                        break
                    check = seats[x+diagonal_check, y-diagonal_check]
                    if check != Floor:
                        surrounding = numpy.append(surrounding, check)
                        break
                    diagonal_check += 1

                diagonal_check = 1
                while True:
                    if x-diagonal_check < 0 or y+diagonal_check >= yRange:
                        break
                    check = seats[x-diagonal_check, y+diagonal_check]
                    if check != Floor:
                        surrounding = numpy.append(surrounding, check)
                        break
                    diagonal_check += 1

                if seats[x][y] == Free:
                    if sum(surrounding == Occupied) == 0:
                        newSeats[x][y] = Occupied
                        changes += 1
                        continue
                if seats[x][y] == Occupied:
                    if sum(surrounding == Occupied) >= 5:
                        newSeats[x][y] = Free
                        changes += 1
                        continue
        print(f"Round {round}, {changes} changes")
        if changes == 0:
            return sum(sum(seats == Occupied))
        seats = newSeats


def main(file="input.txt"):
    seats = load_seats(file)
    return first(seats), second(seats)


if __name__ == '__main__':
    one, two = main()
    assert one == 2166
    assert two == 1955
    print(one)
    print(two)
