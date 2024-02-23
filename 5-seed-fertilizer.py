# S 15 16 17 18 ... 51
# D 0  1  2  3 ... 36

# D  0  1  2  3 ... 36 37 38 39 40 ... 53
# S 15 16 17 18 ... 51 52 53  0  1 ... 14

# 1,310,704,671
#
# 2,879,792,625 0 201,678,008
# 0 201,678,008 400,354,950
# 1,564,640,751 602,032,958 433,757,289
# 2,425,309,256 1,035,790,247 296,756,276
# 1,998,398,040 1,332,546,523 426,911,216
# 2,722,065,532 1,759,457,739 157,727,093
# 400,354,950 1,917,184,832 1,164,285,801
#
# dic 
# 0             : 2,879,792,625
# 201,678,007   : 3,081,470,632
# 201,678,008   : 0
# 602,032,957   : 400,354,949
# 602,032,958   : 1,564,640,751
# 1,035,790,246 : 1,998,398,039
# 1,035,790,247 : 2,425,309,256
# 1,332,546,523 : 1,998,398,040
# 1,759,457,738 : 2,425,309,255
# 1,759,457,739 : 2,722,065,532
# 1,917,184,831 : 2,879,792,624
# 1,917,184,832 : 400,354,950

# 1,310,704,671 - 1,035,790,247 = 274,914,424
# 2,425,309,256 - 274,914,424 = 2,150,394,832

# 50 98 2
# 52 50 48

# dic
# 50 52
# 97 99
# 98 50
# 99 51
from enum import Enum

with open('5-seed-fertilizer-input.txt') as input:
    class Almanac(Enum):
        NONE = 0
        SEED_TO_SOIL = 1
        SOIL_TO_FERTILIZER = 2
        FERTILIZER_TO_WATER = 3
        WATER_TO_LIGHT = 4
        LIGHT_TO_TEMPERATURE = 5
        TEMPERATURE_TO_HUMIDITY = 6
        HUMIDITY_TO_LOCATION = 7

    def extract_number(index, line):
        start_index = index
        while line[start_index].isdigit():
            start_index -= 1
        start_index += 1
        end_index = start_index
        while end_index < len(line) and line[end_index].isdigit():
            end_index += 1
        return int(line[start_index:end_index])

    current_almanac = Almanac.NONE
    seeds = []
    almanacs = [[] for x in range(len(Almanac))]

    for line in input:
        if line == '\n':
            continue
        if line.startswith('seeds:'):
            seeds = line[7:].strip().split(' ')
            continue
        elif line.startswith('seed-to-soil'):
            current_almanac = Almanac.SEED_TO_SOIL
            continue
        elif line.startswith('soil-to-fertilizer'):
            current_almanac = Almanac.SOIL_TO_FERTILIZER
            continue
        elif line.startswith('fertilizer-to-water'):
            current_almanac = Almanac.FERTILIZER_TO_WATER
            continue
        elif line.startswith('water-to-light'):
            current_almanac = Almanac.WATER_TO_LIGHT
            continue
        elif line.startswith('light-to-temperature'):
            current_almanac = Almanac.LIGHT_TO_TEMPERATURE
            continue
        elif line.startswith('temperature-to-humidity'):
            current_almanac = Almanac.TEMPERATURE_TO_HUMIDITY
            continue
        elif line.startswith('humidity-to-location'):
            current_almanac = Almanac.HUMIDITY_TO_LOCATION
            continue

        almanacs[int(current_almanac.value)].append(line.strip().split(' '))
    
    def sort_almanac(x): 
        if len(x) <= 2:
            return 0
        return int(x[1])

    for almanac in almanacs:
        almanac.sort(key=sort_almanac)    

    locations = []

    for seed in seeds:
        current_value = int(seed)
        for almanac_type in list(Almanac):
            if almanac_type == Almanac.NONE:
                continue
            current_almanac = almanacs[int(almanac_type.value)]
            for i, almanac_value in enumerate(current_almanac):
                if int(almanac_value[1]) + int(almanac_value[2]) < current_value:
                    continue
                if current_value > int(almanac_value[1]) + int(almanac_value[2]):
                    print('out of range')
                if int(almanac_value[1]) < current_value:
                    diff = current_value - int(current_almanac[i][1])
                    current_value = int(current_almanac[i][0]) + diff
                if almanac_type == Almanac.HUMIDITY_TO_LOCATION:
                    locations.append(current_value)
                break
    print(min(locations))

