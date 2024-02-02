MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

with open('2-cube-conundrum-input.txt') as input:
    total_power = 0

    for line in input:
        [game, results] = line.split(':')
        [_, game_number] = game.split(' ')
        rounds = list(map(lambda s: s.strip(), results.split(';')))

        min_red = 0
        min_green = 0
        min_blue = 0

        for round in rounds:
            cubes = round.split(', ')
            for cube in cubes:
                [num_cubes_str, cube_color] = cube.split(' ')
                num_cubes = int(num_cubes_str)
                if cube_color == 'red':
                    if num_cubes > min_red:
                        min_red = num_cubes
                elif cube_color == 'green':
                    if num_cubes > min_green:
                        min_green = num_cubes
                else:
                    if num_cubes > min_blue:
                        min_blue = num_cubes
            
        round_power = min_red * min_green * min_blue
        total_power += round_power
    print(total_power)