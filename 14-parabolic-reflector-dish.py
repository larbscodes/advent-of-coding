from pprint import pprint

platform = []

with open('14-parabolic-reflector-dish-input.txt') as input:
    for line in input:
        platform.append(line.strip())

max_load = len(platform)

current_row = 0
current_col = 0

def calc_load(starting_load, num_rocks):
    print(starting_load, num_rocks)
    load = 0
    for _ in range(num_rocks):
        load += starting_load
        starting_load -= 1
    return load

total_load = 0
while current_col < len(platform[0]):
    current_max_load = max_load
    num_rocks = 0
    while current_row < len(platform):
        tile = platform[current_row][current_col]
        if tile == 'O':
            num_rocks += 1

        if tile == '#' or current_row == len(platform) - 1:
            total_load += calc_load(current_max_load, num_rocks)
            current_max_load = max_load - current_row - 1
            num_rocks = 0
        
        current_row += 1
    
    current_row = 0
    current_col += 1
print(total_load)