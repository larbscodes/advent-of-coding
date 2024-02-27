# Time:        44     70     70     80
# Distance:   283   1134   1134   1491

with open('6-wait-for-it-input.txt') as input:
    time = 0
    winning_distance = 0

    for line in input:
        current_number_str = ''
        for c in line:
            if c.isdigit():
                current_number_str += c
        if time == 0:
            time = int(current_number_str)
            current_number_str = ''
        else:
            winning_distance = int(current_number_str)

    found_start = False

    speed = time // 2
    starting_speed = 0

    min_speed = 0
    max_speed = time

    while found_start == False:
        current_speed = (min_speed + max_speed) // 2
        distance = current_speed * (time - current_speed)

        if min_speed > max_speed:
            found_start = True
            starting_speed = min_speed

        if distance < winning_distance:
            # search top half for start of winnings
            min_speed = current_speed + 1
        elif distance > winning_distance:
            # search bottom half for start of winnings
            max_speed = current_speed - 1
        else:
            starting_speed = current_speed
            found_start = True

    found_end = False
    ending_speed = 0
    min_speed = time // 2
    max_speed = time

    while found_end == False:
        current_speed = (min_speed + max_speed) // 2
        distance = current_speed * (time - current_speed)

        if min_speed > max_speed:
            found_end = True
            ending_speed = min_speed

        if distance < winning_distance:
            # search top half for start of winnings
            max_speed = current_speed - 1
        elif distance > winning_distance:
            # search bottom half for start of winnings
            min_speed = current_speed + 1
        else:
            ending_speed = current_speed
            found_end = True

    print(ending_speed - starting_speed)