from pprint import pprint
from copy import deepcopy

dig_plan = []

with open('18-lavaduct-lagoon-input.txt') as input:
    raw_data = []
    for line in input:
        dig_plan.append(line.strip())

current_width = 1
current_height = 1

min_width = 0
min_height = 0
max_width = 1
max_height = 1

for step in dig_plan:
    raw_step = step.split(' ')
    direction = raw_step[0]
    distance = int(raw_step[1])

    if direction == 'R':
        current_width += distance
    elif direction == 'L':
        current_width -= distance
    elif direction == 'U':
        current_height -= distance
    elif direction == 'D':
        current_height += distance
    
    if current_width > max_width:
        max_width = current_width
    elif current_height > max_height:
        max_height = current_height
    elif current_width < min_width:
        min_width = current_width
    elif current_height < min_height:
        min_height = current_height

starting_x = -min_height + 1
starting_y = -min_width + 1
width = max_width - min_width
height = max_height - min_height

lagoon = [ ['.'] * (width + 1) for _ in range(height + 1)]

lagoon[starting_x][starting_y] = '#'

def dig(lagoon, x, y, direction, distance):
    dx = 0
    dy = 0
    if direction == 'R':
        dy = 1
    elif direction == 'L':
        dy = -1
    elif direction == 'U':
        dx = -1
    elif direction == 'D':
        dx = 1
    
    while distance > 0:
        x += dx
        y += dy
        lagoon[x][y] = '#'
        distance -= 1
    
    return (x, y)

current_x = starting_x
current_y = starting_y
for step in dig_plan:
    raw_step = step.split(' ')
    direction = raw_step[0]
    distance = int(raw_step[1])

    (current_x, current_y) = dig(lagoon, current_x, current_y, direction, distance)

def is_enclosed(lagoon, i, j):
    wall_count = 0
    entry_wall_connects_above = False
    entry_wall_connects_below = False
    in_wall = False

    for k in range(j+1, len(lagoon[i])):
        if lagoon[i][k] == '#':
            if not in_wall:
                in_wall = True
                if i == 0:
                    entry_wall_connects_below = True
                elif i == len(lagoon) - 1:
                    entry_wall_connects_above = True
                else:
                    if lagoon[i-1][k] == '#':
                        entry_wall_connects_above = True
                    if lagoon[i+1][k] == '#':
                        entry_wall_connects_below = True
            if entry_wall_connects_above == True and entry_wall_connects_below == True:
                wall_count += 1
                in_wall = False
                entry_wall_connects_above = False
                entry_wall_connects_below = False
        else:
            if in_wall:
                exit_wall_connects_above = False
                if i > 0:
                    if lagoon[i-1][k-1] == '#':
                        exit_wall_connects_above = True
                if entry_wall_connects_above != exit_wall_connects_above:
                    wall_count += 1
                in_wall = False
                entry_wall_connects_above = False
                entry_wall_connects_below = False

    if in_wall and lagoon[i][-1] == '#':
        wall_count += 1
    
    return wall_count % 2 == 1

def dig_consecutive(i, j, lagoon):
    while lagoon[i][j] == '.':
        lagoon[i][j] = '#'
        j += 1

def mark_external(i, j, lagoon):
    while j < len(lagoon[0]) and lagoon[i][j] == '.':
        lagoon[i][j] = ','
        j += 1

modified_lagoon = deepcopy(lagoon)
for i in range(len(lagoon)):
    for j in range(len(lagoon[0])):
        if lagoon[i][j] == '#' or lagoon[i][j] == ',':
            continue
        should_dig = is_enclosed(lagoon, i , j)
        if should_dig:
            dig_consecutive(i, j, modified_lagoon)
        else:
            mark_external(i, j, lagoon)

holes = 0
for row in modified_lagoon:
    for tile in row:
        if tile == '#':
            holes += 1

print(holes)