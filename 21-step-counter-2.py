from pprint import pprint
from collections import namedtuple

garden = []
starting_x = 0
starting_y = 0

Multipliers = namedtuple('Multipliers', ' x y')
PlotPosition = namedtuple('State', 'x y multipliers')

with open('step-counter-input.txt') as input:
    for i, line in enumerate(input):
        line = line.strip()

        if 'S' in line:
            starting_x = i
            starting_y = line.index('S')

        garden.append(list(line))

def update_plot_positions(current_plots, incoming_plots):
    plots = current_plots
    new_plots = []
    for incoming_plot in incoming_plots:
        found_match = False
        for i in range(len(current_plots)):
            if current_plots[i].x == incoming_plot.x and current_plots[i].y == incoming_plot.y:
                plots[i] = PlotPosition(plots[i].x, plots[i].y, tuple(set().union(current_plots[i].multipliers, incoming_plot.multipliers)))
                found_match = True
                break
        if not found_match:
            new_plots.append(incoming_plot)
    return set(plots + new_plots)

dp = [ [[]] * len(garden[0]) for _ in range(len(garden)) ]

garden_height = len(garden)
garden_width = len(garden[0])
steps = 100
plot_spots = [PlotPosition(starting_x, starting_y, tuple([Multipliers(0,0)]))]
while steps > 0:
    print(len(plot_spots))
    next_plots = set()
    while plot_spots:
        x, y, multipliers = plot_spots.pop(0)

        if dp[x][y]:
            next_plots.update(dp[x][y])
            continue

        adjacent_plots = set()
        if x > 0 and garden[x-1][y] != '#':
            adjacent_plots.add(PlotPosition(x-1, y, multipliers))
        elif x == 0 and garden[-1][y] != '#':
            new_multipliers = tuple(map(lambda mult: (mult.x - 1, mult.y), multipliers))
            adjacent_plots.add(PlotPosition(garden_height - 1, y, multipliers+new_multipliers))

        if x < len(garden) - 1 and garden[x+1][y] != '#':
            adjacent_plots.add(PlotPosition(x+1, y, multipliers))
        elif x == len(garden) - 1 and garden[0][y] != '#':
            new_multipliers = tuple(map(lambda mult: (mult.x + 1, mult.y), multipliers))
            adjacent_plots.add(PlotPosition(0, y, new_multipliers))

        if y  > 0 and garden[x][y-1] != '#':
            adjacent_plots.add(PlotPosition(x, y-1, multipliers))
        elif y == 0 and garden[x][-1] != '#':
            new_multipliers = tuple(map(lambda mult: (mult.x, mult.y - 1), multipliers))
            adjacent_plots.add(PlotPosition(x, garden_width - 1, multipliers+new_multipliers))

        if y < garden_width - 1 and garden[x][y+1] != '#':
            adjacent_plots.add(PlotPosition(x, y+1, multipliers))
        elif y == garden_width - 1 and garden[x][0] != '#':
            new_multipliers = tuple(map(lambda mult: (mult.x, mult.y + 1), multipliers))
            adjacent_plots.add(PlotPosition(x, 0, new_multipliers))

        pprint(len(adjacent_plots))
        # if there are x,y matches from adjacent_plots to next_plots, use the union of the multiplier lists
        next_plots.update(update_plot_positions(list(next_plots), list(adjacent_plots)))
        dp[x][y] = next_plots
    plot_spots = list(next_plots)
    steps -= 1