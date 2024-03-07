from enum import Enum

with open('10-pipe-maze-input.txt') as input:

    class Direction(Enum):
        NONE = 0
        North = 1
        South = 2
        East = 3
        West = 4

    maze = []

    line_num = 0
    starting_row = 0
    starting_col = 0
    for line in input:
        if 'S' in line:
            starting_row = line_num
            starting_col = line.index('S')
        maze.append(line.strip())
        line_num += 1
    
    def connects_south(pipe):
        if pipe == '|' or pipe == 'L' or pipe == 'J':
            return True
        return False
    
    def connects_north(pipe):
        if pipe == '|' or pipe == '7' or pipe == 'F':
            return True
        return False

    def connects_east(pipe):
        if pipe == '7' or pipe == 'J' or pipe == '-':
            return True
        return False
    
    def connects_west(pipe):
        if pipe == 'L' or pipe == 'F' or pipe == '-':
            return True
        return False

    def find_next_point(maze, x, y, coming_from = Direction.NONE):
        if connects_north(maze[x-1][y]) and coming_from != Direction.North:
            return (x-1, y, Direction.South)
        elif connects_south(maze[x+1][y]) and coming_from != Direction.South:
            return (x+1, y, Direction.North)
        elif connects_east(maze[x][y+1]) and coming_from != Direction.East:
            return (x, y+1, Direction.West)
        elif connects_west(maze[x][y-1]) and coming_from != Direction.West: 
            return (x, y-1, Direction.East)
        return (x, y, Direction.NONE)


    starting_point_info = find_next_point(maze, starting_row, starting_col)
    
    loop_length = 1
    current_x = starting_point_info[0]
    current_y = starting_point_info[1]
    current_pipe = maze[current_x][current_y]

    coming_from = starting_point_info[2]

    while current_pipe != 'S':
        loop_length += 1

        if current_pipe == '|':
            if coming_from == Direction.North:
                current_x += 1
                coming_from = Direction.North
            else:
                current_x -= 1
                coming_from = Direction.South
        elif current_pipe == 'L':
            if coming_from == Direction.North:
                current_y += 1
                coming_from = Direction.West
            else:
                current_x -= 1
                coming_from = Direction.South
        elif current_pipe == 'J':
            if coming_from == Direction.North:
                current_y -= 1
                coming_from = Direction.East
            else:
                current_x -= 1
                coming_from = Direction.South
        elif current_pipe == '-':
            if coming_from == Direction.West:
                current_y += 1
                coming_from = Direction.West
            else:
                current_y -= 1
                coming_from = Direction.East
        elif current_pipe == '7':
            if coming_from == Direction.South:
                current_y -= 1
                coming_from = Direction.East
            else:
                current_x += 1
                coming_from = Direction.North
        elif current_pipe == 'F':
            if coming_from == Direction.South:
                current_y += 1
                coming_from = Direction.West
            else:
                current_x += 1
                coming_from = Direction.North
        current_pipe = maze[current_x][current_y]
    
    print(loop_length//2)