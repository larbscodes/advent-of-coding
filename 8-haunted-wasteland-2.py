import numpy as np

with open('8-haunted-wasteland-input.txt') as input:
    
    def extract_start(line):
        return line[:3]

    def extract_left(line):
        return line[7:10]
    
    def extract_right(line):
        return line[12:15]

    instructions = ''
    network = {}

    for line in input:
        if instructions == '':
            instructions = line.strip()
            continue
        if line == '\n':
            continue

        network[extract_start(line)] = (extract_left(line), extract_right(line))
    
    starting_locations = []
    for loc in list(network.keys()):
        if loc[-1] == 'A':
            starting_locations.append(loc)

    step_count = 0
    index = 0
    max_index = len(instructions) - 1
    current_location = ''
    step_counts = []

    for location in starting_locations:
        current_location = location
        while current_location[-1] != 'Z':
            step = instructions[index]
            if step == 'L':
                current_location = network[current_location][0]
            elif step == 'R':
                current_location = network[current_location][1]
            
            if index < max_index:
                index +=1
            else:
                index = 0

            step_count += 1
        
        step_counts.append(step_count)
        index = 0
        step_count = 0

    print(step_counts)

    print(np.lcm.reduce(step_counts))