# Time:        44     70     70     80
# Distance:   283   1134   1134   1491
#
# max = 44
# 1 * 43
# 2 * 42
# 3 * 41
# 4 * 40

with open('6-wait-for-it-input.txt') as input:
    times = []
    distances = []

    for line in input:
        current_number_str = ''
        for c in line:
            if c.isdigit():
                current_number_str += c
            elif current_number_str != '' and line.startswith('Time:'):
                current_number = int(current_number_str)
                current_number_str = ''
                times.append(current_number)
            elif current_number_str != '' and line.startswith('Distance:'):
                current_number_str += c
                current_number = int(current_number_str)
                current_number_str = ''
                distances.append(current_number)

    error_margin = 1

    for i, time in enumerate(times):
        wins = 0
        for j in range(time):
            speed = j
            moving_time = time - j
            distance = speed * moving_time
            if distance > distances[i]:
                wins += 1
            elif wins > 0:
                break
        error_margin *= wins
        wins = 0
    
    print(error_margin)
    