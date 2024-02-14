with open('3-gear-ratios-input.txt') as input:
    prev = ''
    current = ''
    next = ''

    total = 0

    for line in input:
        prev = current
        current = next
        next = line

        if current == '':
            continue

        indices = []
        start_index = -1
        length = 0
        for i, char in enumerate(current):
            if char.isdigit():
                if start_index == -1:
                    start_index = i
                length += 1
            else:
                if start_index >= 0 and length > 0:
                    indices.append((start_index, length, int(current[start_index:start_index+length])))
                start_index = -1
                length = 0

        for tuple in indices:
            max_index = len(current) - 1

            number_used = False
            start_index = tuple[0]
            end_index = tuple[0] + tuple[1]

            if prev != '':
                for i in range(start_index-1, end_index+1):
                    if i == max_index or i < 0:
                        continue
                    if prev[i].isdigit() == False and prev[i] != '.':
                        total += tuple[2]
                        number_used = True
                        break
            if number_used:
                continue

            for i in range(start_index-1, end_index+1):
                if i == max_index or i < 0:
                        continue
                if next[i].isdigit() == False and next[i] != '.':
                    total += tuple[2]
                    number_used = True
                    break
            if number_used:
                continue

            if start_index > 0:
                if current[start_index-1].isdigit() == False and current[start_index-1] != '.':
                    total += tuple[2]
                    number_used = True
            if number_used:
                continue

            if end_index < max_index:
                if current[end_index].isdigit() == False and current[end_index] != '.':
                    total += tuple[2]
                    number_used = True
    print(total)