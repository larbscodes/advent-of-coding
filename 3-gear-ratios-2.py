with open('3-gear-ratios-input.txt') as input:

    def extract_number(index, line):
        start_index = index
        while line[start_index].isdigit():
            start_index -= 1
        start_index += 1
        end_index = start_index
        while line[end_index].isdigit():
            end_index += 1
        return int(line[start_index:end_index])

    prev = ''
    current = ''
    next = ''


    total_ratio = 0

    for line in input:
        prev = current
        current = next
        next = line

        if current == '':
            continue

        max_index = len(current) - 1

        for i, char in enumerate(current):
            gear_parts = 0
            gear_ratio = 1
            if prev != '' and char == '*':
                if prev[i].isdigit():
                    gear_parts += 1
                    gear_ratio *= extract_number(i, prev)
                else: 
                    if i > 0 and prev[i-1].isdigit():
                        gear_parts += 1
                        gear_ratio *= extract_number(i-1, prev)
                    if i < max_index and prev[i+1].isdigit():
                        gear_parts += 1
                        gear_ratio *= extract_number(i+1, prev)
                if next[i].isdigit():
                    gear_parts += 1
                    gear_ratio *= extract_number(i, next)
                else:
                    if i > 0 and next[i-1].isdigit():
                        gear_parts += 1
                        gear_ratio *= extract_number(i-1, next)
                    if i < max_index and next[i+1].isdigit():
                        gear_parts += 1
                        gear_ratio *= extract_number(i+1, next)  
                if i > 0 and current[i-1].isdigit():
                    gear_parts += 1
                    gear_ratio *= extract_number(i-1, current)
                if i < max_index and current[i+1].isdigit():
                    gear_parts += 1
                    gear_ratio *= extract_number(i+1, current)
                if gear_parts == 2:
                    total_ratio += gear_ratio
    print(total_ratio)