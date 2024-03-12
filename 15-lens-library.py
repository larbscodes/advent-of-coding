sequence = []

with open('15-lens-library-input.txt') as input:
    raw_file = input.read()
    sequence = raw_file.strip().split(',')

total_hash = 0
for word in sequence:
    hash_value = 0
    for c in word:
        hash_value += ord(c)
        hash_value *= 17
        hash_value = hash_value % 256
    total_hash += hash_value

print(total_hash)