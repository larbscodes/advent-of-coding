from pprint import pprint
from enum import Enum
from copy import deepcopy

class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

contraption = []

with open('16-the-floor-will-be-lava-input.txt') as input:
    for line in input:
        contraption.append(list(line.strip()))

def bounce_mirror(mirror, direction):
    if direction == Direction.UP:
        return Direction.RIGHT if mirror == '/' else Direction.LEFT
    elif direction == Direction.DOWN:
        return Direction.LEFT if mirror == '/' else Direction.RIGHT
    elif direction == Direction.LEFT:
        return Direction.DOWN if mirror == '/' else Direction.UP
    else:
        return Direction.UP if mirror == '/' else Direction.DOWN

def shoot_beam(contraption, from_x, from_y, direction, visited_mirrors):
    # termination rules
    stop_beam = False
    current_x = from_x
    current_y = from_y
    current_direction = direction

    while not stop_beam:
        current_square = contraption[current_x][current_y]

        if current_square == '.':
            contraption[current_x][current_y] = '#'
        elif current_square == '|':
            if current_direction == Direction.LEFT or current_direction == Direction.RIGHT:
                visited_mirrors[(current_x, current_y)] += 1
                if visited_mirrors[(current_x, current_y)] <= 1:
                    return [(current_x, current_y, Direction.UP), (current_x, current_y, Direction.DOWN)]
                else: return []
            else:
                visited_mirrors[(current_x, current_y)] += 1
        elif current_square == '-':
            if current_direction == Direction.UP or current_direction == Direction.DOWN:
                visited_mirrors[(current_x, current_y)] += 1
                if visited_mirrors[(current_x, current_y)] <= 1:
                    return [(current_x, current_y, Direction.LEFT), (current_x, current_y, Direction.RIGHT)]
                else: return []
            else:
                visited_mirrors[(current_x, current_y)] += 1
        elif current_square == '/' or current_square == '\\':
            current_direction = bounce_mirror(current_square, current_direction)
            visited_mirrors[(current_x, current_y)] = True

        if current_direction == Direction.UP:
            if current_x == 0:
                stop_beam = True
            else:
                current_x -= 1
        elif current_direction == Direction.DOWN:
            if current_x == len(contraption) - 1:
                stop_beam = True
            else:
                current_x += 1
        elif current_direction == Direction.LEFT:
            if current_y == 0:
                stop_beam = True
            else:
                current_y -= 1
        elif current_direction == Direction.RIGHT:
            if current_y == len(contraption[0]) - 1:
                stop_beam = True
            else:
                current_y += 1
        else:
            stop_beam = True
    return []


def count_energized_tiles(contraption, from_x, from_y, direction):
    beams = [(from_x, from_y , direction)]
    visited_mirrors = {}

    for i in range(len(contraption)):
        for j in range(len(contraption[i])):
            visited_mirrors[(i, j)] = 0

    while beams:
        current_beam = beams.pop()
        new_beams = shoot_beam(contraption, current_beam[0], current_beam[1], current_beam[2], visited_mirrors)
        if new_beams:
            beams += new_beams

    for key, value in visited_mirrors.items():
        if value > 0:
            contraption[key[0]][key[1]] = '#'

    count = 0
    for row in contraption:
        for tile in row:
            if tile == '#':
                count += 1
    return count

max_tiles = 0
for direction in Direction:
    if direction == Direction.UP:
        for col in range(len(contraption[0])):
            fresh_contraption = deepcopy(contraption)
            tiles = count_energized_tiles(fresh_contraption, len(contraption) - 1, col, direction)
            if tiles > max_tiles:
                max_tiles = tiles
    elif direction == Direction.DOWN:
        for col in range(len(contraption[0])):
            fresh_contraption = deepcopy(contraption)
            tiles = count_energized_tiles(fresh_contraption, 0, col, direction)
            if tiles > max_tiles:
                max_tiles = tiles
    elif direction == Direction.LEFT:
        for row in range(len(contraption)):
            fresh_contraption = deepcopy(contraption)
            tiles = count_energized_tiles(fresh_contraption, row, len(contraption[0]) - 1, direction)
            if tiles > max_tiles:
                max_tiles = tiles
    elif direction == Direction.RIGHT:
        for row in range(len(contraption)):
            fresh_contraption = deepcopy(contraption)
            tiles = count_energized_tiles(fresh_contraption, row, 0, direction)
            if tiles > max_tiles:
                max_tiles = tiles
print(max_tiles)