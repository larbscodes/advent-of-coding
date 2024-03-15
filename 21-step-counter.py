from pprint import pprint
from collections import namedtuple

garden = []
starting_x = 0
starting_y = 0

PlotPosition = namedtuple('State', 'x y')

with open('step-counter-input.txt') as input:
    for i, line in enumerate(input):
        line = line.strip()

        if 'S' in line:
            starting_x = i
            starting_y = line.index('S')

        garden.append(list(line))

dp = [ [[]] * len(garden[0]) for _ in range(len(garden)) ]

steps = 65
plot_spots = [PlotPosition(starting_x, starting_y)]
while steps > 0:
    pprint(len(plot_spots))
    next_plots = set()
    while plot_spots:
        x, y = plot_spots.pop(0)

        if dp[x][y]:
            next_plots.update(dp[x][y])
            continue

        adjacent_plots = set()
        if x > 0 and garden[x-1][y] != '#':
            adjacent_plots.add(PlotPosition(x-1, y))
        if x < len(garden) - 1 and garden[x+1][y] != '#':
            adjacent_plots.add(PlotPosition(x+1, y))
        if y > 0 and garden[x][y-1] != '#':
            adjacent_plots.add(PlotPosition(x, y-1))
        if y < len(garden[0]) - 1 and garden[x][y+1] != '#':
            adjacent_plots.add(PlotPosition(x, y+1))
        next_plots.update(adjacent_plots)
        dp[x][y] = adjacent_plots
    plot_spots = list(next_plots)
    steps -= 1