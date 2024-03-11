from pprint import pprint
from copy import deepcopy

platform = []

with open('14-parabolic-reflector-dish-input.txt') as input:
    for line in input:
        platform.append(list(line.strip()))

def calc_load(starting_load, num_rocks):
    load = 0
    for _ in range(num_rocks):
        load += starting_load
        starting_load -= 1
    return load

def cycle(platform):
    return tilt_east(tilt_south(tilt_west(tilt_north(platform))))

def tilt_north(platform):
    updated_platform = deepcopy(platform)
    current_row = 0
    current_col = 0
    while current_col < len(platform[0]):
        rocks_to_add = 0
        next_rock_index = 0
        while current_row < len(platform):
            tile = platform[current_row][current_col]
            if tile == 'O':
                rocks_to_add += 1

            if tile == '#' or current_row == len(platform) - 1:
                for i in range(next_rock_index, current_row + 1):
                    if rocks_to_add > 0:
                        updated_platform[i][current_col] = 'O'
                        rocks_to_add -= 1
                    elif platform[i][current_col] != '#':
                        updated_platform[i][current_col] = '.'
                next_rock_index = current_row + 1
                rocks_to_add = 0
            
            current_row += 1
        
        current_row = 0
        current_col += 1
    
    return updated_platform

def tilt_south(platform):
    num_rows = len(platform)
    updated_platform = deepcopy(platform)
    current_row = num_rows - 1
    current_col = 0
    while current_col < len(platform[0]):
        rocks_to_add = 0
        next_rock_index = num_rows - 1
        while current_row >= 0:
            tile = platform[current_row][current_col]
            if tile == 'O':
                rocks_to_add += 1

            if tile == '#' or current_row == 0:
                for i in range(next_rock_index, current_row - 1, -1):
                    if rocks_to_add > 0:
                        updated_platform[i][current_col] = 'O'
                        rocks_to_add -= 1
                    elif platform[i][current_col] != '#':
                        updated_platform[i][current_col] = '.'
                next_rock_index = current_row - 1
                rocks_to_add = 0
            
            current_row -= 1
        
        current_row = num_rows - 1
        current_col += 1
    
    return updated_platform

def tilt_west(platform):
    updated_platform = deepcopy(platform)
    current_col = 0

    for i, row in enumerate(platform):
        rocks_to_add = 0
        next_rock_index = 0
        while current_col < len(row):
            tile = row[current_col]
            if tile == 'O':
                rocks_to_add += 1

            if tile == '#' or current_col == len(row) - 1:
                for j in range(next_rock_index, current_col + 1):
                    if rocks_to_add > 0:
                        updated_platform[i][j] = 'O'
                        rocks_to_add -= 1
                    elif row[j] != '#':
                        updated_platform[i][j] = '.'
                next_rock_index = current_col + 1
                rocks_to_add = 0
            
            current_col += 1
        current_col = 0
    
    return updated_platform

def tilt_east(platform):
    updated_platform = deepcopy(platform)

    for i, row in enumerate(platform):
        rocks_to_add = 0
        current_col = len(row) - 1
        next_rock_index = current_col
        while current_col >= 0:
            tile = row[current_col]
            if tile == 'O':
                rocks_to_add += 1

            if tile == '#' or current_col == 0:
                for j in range(next_rock_index, current_col - 1, -1):
                    if rocks_to_add > 0:
                        updated_platform[i][j] = 'O'
                        rocks_to_add -= 1
                    elif row[j] != '#':
                        updated_platform[i][j] = '.'
                next_rock_index = current_col - 1
                rocks_to_add = 0
            
            current_col -= 1
    
    return updated_platform

platforms = [platform]
found = False
cycles = 0
while not found:
    cycles += 1
    next_platform = cycle(platforms[-1])
    if next_platform in platforms:
        found = True
    
    platforms.append(next_platform)

first_index = platforms.index(platforms[-1])
second_index = len(platforms) - 1

remainder = (1000000000 - first_index) % (second_index - first_index)

key_platform = platforms[first_index + remainder]
total_load = 0
for i, row in enumerate(key_platform):
    load_for_row = len(key_platform) - i
    for tile in row:
        if tile == 'O':
            total_load += load_for_row

print(total_load)