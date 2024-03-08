with open('11-cosmic-expansion-input.txt') as input:
    row_counts_as_double = {}
    col_counts_as_double = {}

    image = []
    galaxies = []

    row_index = 0

    for line in input:
        if '#' in line:
            row_counts_as_double[row_index] = False
        else:
            row_counts_as_double[row_index] = True

        image.append([])
        
        for col_index, c in enumerate(line.strip()):
            if c == '#':
                col_counts_as_double[col_index] = False
                galaxies.append((row_index, col_index))
            elif col_index not in col_counts_as_double:
                col_counts_as_double[col_index] = True
            image[row_index].append(c)

        row_index += 1

    def distance_between_galaxies(gal1, gal2):
        extra_distance = 0

        row_range = range(gal1[0], gal2[0])
        if gal1[0] > gal2[0]:
            row_range = range(gal2[0], gal1[0])

        col_range = range(gal1[1], gal2[1])
        if gal1[1] > gal2[1]:
            col_range = range(gal2[1], gal1[1])

        for row in row_range:
            if row_counts_as_double[row] == True:
                extra_distance += 1
        
        for col in col_range:
            if col_counts_as_double[col] == True:
                extra_distance += 1

        return abs(gal2[1] - gal1[1]) + abs(gal2[0] - gal1[0]) + extra_distance

    total_distance = 0
    for i, galaxy in enumerate(galaxies):
        for j in range(i+1, len(galaxies)):
            total_distance += distance_between_galaxies(galaxy, galaxies[j])
    
    print(total_distance)