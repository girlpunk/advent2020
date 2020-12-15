import math

def load_instructions(file):
    return [[line[0], int(line[1:])] for line in open(file)]


def first(instructions):
    facing = 0
    eastings = 0
    northings = 0
    for instruction in instructions:
        if instruction[0] == 'N':
            northings += instruction[1]
        elif instruction[0] == 'S':
            northings -= instruction[1]
        elif instruction[0] == 'E':
            eastings += instruction[1]
        elif instruction[0] == 'W':
            eastings -= instruction[1]
        elif instruction[0] == 'L':
            facing -= (instruction[1] / 90)
        elif instruction[0] == 'R':
            facing += (instruction[1] / 90)
        elif instruction[0] == 'F':
            facing %= 4
            if facing == 0:
                eastings += instruction[1]
            elif facing == 1:
                northings -= instruction[1]
            elif facing == 2:
                eastings -= instruction[1]
            elif facing == 3:
                northings += instruction[1]
    return abs(northings) + abs(eastings)


def second(instructions):
    waypoint_eastings = 10
    waypoint_northings = 1
    ship_eastings = 0
    ship_northings = 0
    for instruction in instructions:
        if instruction[0] == 'N':
            waypoint_northings += instruction[1]
        elif instruction[0] == 'S':
            waypoint_northings -= instruction[1]
        elif instruction[0] == 'E':
            waypoint_eastings += instruction[1]
        elif instruction[0] == 'W':
            waypoint_eastings -= instruction[1]
        elif instruction[0] == 'L':
            angle = -math.radians(instruction[1])
            d_northings = ship_northings + math.cos(angle) * (waypoint_northings - ship_northings) - math.sin(angle) * (waypoint_eastings - ship_eastings)
            d_eastings  = ship_eastings  + math.sin(angle) * (waypoint_northings - ship_northings) + math.cos(angle) * (waypoint_eastings - ship_eastings)
            waypoint_northings = int(d_northings)
            waypoint_eastings = int(d_eastings)
        elif instruction[0] == 'R':
            angle = math.radians(instruction[1])
            d_northings = ship_northings + math.cos(angle) * (waypoint_northings - ship_northings) - math.sin(angle) * (waypoint_eastings - ship_eastings)
            d_eastings  = ship_eastings  + math.sin(angle) * (waypoint_northings - ship_northings) + math.cos(angle) * (waypoint_eastings - ship_eastings)
            waypoint_northings = int(d_northings)
            waypoint_eastings = int(d_eastings)
        elif instruction[0] == 'F':
            d_northings = (waypoint_northings - ship_northings) * instruction[1]
            d_eastings  = (waypoint_eastings - ship_eastings) * instruction[1]
            ship_northings += d_northings
            ship_eastings  += d_eastings
            waypoint_northings += d_northings
            waypoint_eastings  += d_eastings
    return int(abs(ship_northings) + abs(ship_eastings))


def main(file="input.txt"):
    instructions = load_instructions(file)
    return first(instructions), second(instructions)


if __name__ == '__main__':
    one, two = main()
    assert one == 2057
    assert two == 77730285
    print(one)
    print(two)
