import functools

with open('12-hot-springs-input.txt') as input:

    @functools.cache
    def calc(springs, damaged_groups):
        if not damaged_groups:
            if '#' not in springs:
                return 1
            else:
                return 0
        
        if not springs:
            return 0

        # Look at the next element in each record and group
        next_character = springs[0]
        next_group_len = damaged_groups[0]

        def pound():
            this_group = springs[:next_group_len]
            this_group = this_group.replace("?", "#")

            if this_group != next_group_len * "#":
                return 0
            
            # How I would write it
            if len(this_group) != next_group_len or not all(spring == '#' or spring == '?' for spring in this_group):
                return 0

            if len(springs) == next_group_len:
                if len(damaged_groups) == 1:
                    return 1
                else:
                    return 0
            
            next_spring = springs[next_group_len]
            if next_spring in '?.':
                return calc(springs[next_group_len + 1:], damaged_groups[1:])
            
            return 0


        def dot():
            return calc(springs[1:], damaged_groups)
        
        if next_character == '#':
            return pound()
        elif next_character == '.':
            return dot()
        else:
            return pound() + dot()

    arrangements = 0
    for line in input:
        [springs, contiguous_damaged_springs_input] = line.strip().split(' ')
        contiguous_damaged_springs = list(map(lambda x: int(x), contiguous_damaged_springs_input.split(',')))
        arrangements += calc(springs, tuple(contiguous_damaged_springs))
    
    print(arrangements)