from pprint import pprint
sequence = []

with open('15-lens-library-input.txt') as input:
    raw_file = input.read()
    sequence = raw_file.strip().split(',')

total_hash = 0
boxes = [[] for i in range(256)]

for step in sequence:
    label = ''
    lens = 0
    if '=' in step:
        [label, raw_lens] = step.split('=')
        lens = int(raw_lens)
    elif '-' in step:
        label = step[:-1]
    else:
        continue

    hash_value = 0
    for c in label:
        hash_value += ord(c)
        hash_value *= 17
        hash_value = hash_value % 256

    labels = list(map(lambda x: x[0], boxes[hash_value]))
    if lens > 0:
        if label in labels:
            matching_index = labels.index(label)
            boxes[hash_value][matching_index] = (label, lens)
        else:
            boxes[hash_value].append((label, lens))
    else:
        if label in labels:
            matching_index = labels.index(label)
            del boxes[hash_value][matching_index]

total_focusing_power = 0
for i, box in enumerate(boxes):
    if len(box) == 0:
        continue
    box_num = i + 1
    for j, lens in enumerate(box):
        focal_length = lens[1]
        slot_num = j + 1
        focusing_power = box_num * slot_num * focal_length
        total_focusing_power += focusing_power
print(total_focusing_power)