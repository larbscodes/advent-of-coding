from itertools import pairwise

GridPoint = tuple[int, int]

OFFSETS = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}

OFFSET_INDEXES = list(OFFSETS.values())

def add_points(a: GridPoint, b: GridPoint) -> GridPoint:
    """
    add a pair of 2-tuples together. Useful for calculating a new position from a location and an offset
    """
    return a[0] + b[0], a[1] + b[1]

def num_points(outline: list[GridPoint], border_length: int) -> int:
    # shoelace - find the float area in a shape
    area = (
        sum(
            row1 * col2 - row2 * col1
            for (row1, col1), (row2, col2) in pairwise(outline)
        )
        / 2
    )
    # pick's theorem - find the number of points in a shape given its area
    return int(abs(area) - 0.5 * border_length + 1) + border_length

with open('18-lavaduct-lagoon-input.txt') as input:
    outline: list[GridPoint] = [(0, 0)]
    border_length = 0

    for line in input:
        _, _, hex_str = line.split()

        distance = int(hex_str[2:-2], 16)

        offset = OFFSET_INDEXES[int(hex_str[-2])]
        scaled_offset = (offset[0] * distance, offset[1] * distance)
        outline.append(add_points(scaled_offset, outline[-1]))
        border_length += distance

    print(num_points(outline, border_length))