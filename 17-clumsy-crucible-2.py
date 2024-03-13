from pprint import pprint
import heapq
from collections import namedtuple
import sys

ScoredState = namedtuple('State', 'heat_loss x y dx dy distance')
State = namedtuple('State', 'x y dx dy distance')

city = []

with open('17-clumsy-crucible-input.txt') as input:
    raw_data = []
    for line in input:
        int_line = list(map(lambda x: int(x), list(line.strip())))
        city.append(int_line)

city_width = len(city[0])
city_height = len(city)
max_x = city_height - 1
max_y = city_width - 1

# heat_loss position direction length

heap: list[ScoredState] = []
min_heat_loss: dict[State, int] = {}
visited: dict[State, bool] = {}

state1 = ScoredState(city[1][0], 1, 0, 1, 0, 1)
state2 = ScoredState(city[0][1], 0, 1, 0, 1, 1)
heapq.heappush(heap, state1)
heapq.heappush(heap, state2)
min_heat_loss[State(1, 0, 1, 0, 1)] = city[1][0]
min_heat_loss[State(0, 1, 0, 1, 1)] = city[0][1]

counter = 0

while heap:
    processed_state = heapq.heappop(heap)
    (heat_loss, x, y, dx, dy, distance) = processed_state
    visited[State(x, y, dx, dy, distance)] = True
    next_moves = []
    if distance < 10:
        next_moves.append((dx, dy, distance + 1))
    if distance >= 4:
        next_moves += [(dy, -dx, 1), (-dy, dx, 1)]
    
    for move in next_moves:
        (next_dx, next_dy, next_distance) = move
        next_x = x + next_dx
        next_y = y + next_dy

        if next_x < 0 or next_y < 0:
            continue
        if next_x > max_x or next_y > max_y:
            continue
        if next_x == max_x and next_y == max_y and next_distance >= 4:
            print(heat_loss + city[next_x][next_y])

        next_heat_loss = heat_loss + city[next_x][next_y]
        new_state = State(x + next_dx, y + next_dy, next_dx, next_dy, next_distance)
        new_scored_state = ScoredState(next_heat_loss, x + next_dx, y + next_dy, next_dx, next_dy, next_distance)

        if new_state not in visited:
            if new_state in min_heat_loss:
                if min_heat_loss[new_state] > next_heat_loss:
                    min_heat_loss[new_state] = next_heat_loss
                    heapq.heappush(heap, new_scored_state)
            else:
                min_heat_loss[new_state] = next_heat_loss
                heapq.heappush(heap, new_scored_state)
