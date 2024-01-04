import re

     
#    | is a vertical pipe connecting north and south.
#    - is a horizontal pipe connecting east and west.
#    L is a 90-degree bend connecting north and east.
#    J is a 90-degree bend connecting north and west.
#    7 is a 90-degree bend connecting south and west.
#    F is a 90-degree bend connecting south and east.
#    . is ground; there is no pipe in this tile.
#    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
pipe_dict = {'|': [(-1, 0), (1, 0)],
             '-': [(0, -1), (0, 1)],
             'L': [(-1, 0), (0, 1)],
             'J': [(-1, 0), (0, -1)],
             '7': [(1, 0), (0, -1)],
             'F': [(1, 0), (0, 1)],
             '.': [],
             'S': [(0, 1), (1, 0), (0, -1), (-1, 0)],
            }

def get_next_pos(grid, pos, prev):
    # get pipe connections
    positions = get_pipe_connections(grid, pos)
    #print(f"Positions: {positions}, prev: {prev}")
    # remove the previous position
    positions.remove(prev)
    return positions[0]

def get_pipe_connections(grid, pos):
    # get the pipe
    pipe = grid[pos[0]][pos[1]]
    # get pipe directions
    directions = pipe_dict[pipe]
    # map directions to positions
    positions = [(pos[0] + d[0], pos[1] + d[1]) for d in directions]
    return positions

def get_start_connections(grid, start_pos):
    possible_connections = get_pipe_connections(grid, start_pos)
    connected = []
    for position in possible_connections:
        pipe_connections = get_pipe_connections(grid, position)
        if start_pos in pipe_connections:
            connected.append(position)
    
    print(f"Start connections: {connected}")
    return connected

def print_grid(grid):
    g = [''.join(row) for row in grid]
    print('\n'.join(g))

def part_1(lines):
    grid = [list(line.strip()) for line in lines ]
    #print_grid(grid)

    # find start position
    for i, row in enumerate(grid):
        if 'S' in row:
            start = (i, row.index('S'))
            break

    print(f"Start: {start}")
    connected = get_start_connections(grid, start)

    # arbitrarily choose direction
    position = connected[0]
    prev = start
    distance = 1

    # keep going until we hit the start again
    while grid[position[0]][position[1]] != 'S':
        # get the next position from the grid
        new_position = get_next_pos(grid, position, prev)
        prev = position
        position = new_position

        distance += 1
    
    # the furthest point is half the loop length
    return distance/2

    
def part_2(lines):
    grid = [list(line.strip()) for line in lines ]

    # find start position
    for i, row in enumerate(grid):
        if 'S' in row:
            start = (i, row.index('S'))
            break

    print(f"Start: {start}")
    connected = get_start_connections(grid, start)
    # based on start connections, determine type of pipe
    diffs = [(c[0] - start[0], c[1] - start[1]) for c in connected]
    # find a matching pipe in the pipe dict
    for pipe, directions in pipe_dict.items():
        if set(diffs) == set(directions):
            start_pipe = pipe
            break

    # arbitrarily choose direction
    position = connected[0]
    prev = start

    # copy the grid
    marked_grid = [row[:] for row in grid]
    marked_grid[start[0]][start[1]] = 'X'

    # keep going until we hit the start again
    while grid[position[0]][position[1]] != 'S':
        marked_grid[position[0]][position[1]] = 'X'
        # get the next position from the grid
        new_position = get_next_pos(grid, position, prev)
        prev = position
        position = new_position

    # now classify non-marked positions as inner or outer using a scanline approach
    #print_grid(marked_grid)
    num_inside = 0
    # scan each line
    for i, row in enumerate(marked_grid):
        # records whether currently inside/outside grid
        inside = False
        last_corner = None
        # scan character by character
        for j, col in enumerate(row):
            if col == 'X':
                # determine pipe type
                pipe = grid[i][j]
                if pipe == 'S':
                    pipe = start_pipe
                
                # handle boundary cases
                if last_corner is None:
                    inside = not inside
                    if pipe == 'L' or pipe == 'F':
                        last_corner = pipe
                elif last_corner == 'L':
                    if pipe == 'J':
                        inside = not inside
                        last_corner = None
                    elif pipe == '7':
                        # don't modify inside
                        last_corner = None
                elif last_corner == 'F':
                    if pipe == '7':
                        inside = not inside
                        last_corner = None
                    elif pipe == 'J':
                        # don't modify inside
                        last_corner = None
            elif inside:
                # inside
                grid[i][j] = 'I'
                num_inside += 1
            else:
                # outside
                grid[i][j] = 'O'

    #print_grid(grid)
    return num_inside

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('test_2.txt', 'r') as f:
        test_2_lines = f.readlines()

    with open('test_3.txt', 'r') as f:
        test_3_lines = f.readlines()

    with open('test_4.txt', 'r') as f:
        test_4_lines = f.readlines()

    with open('test_5.txt', 'r') as f:
        test_5_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    test_vals = part_1(test_2_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_3_lines)
    print(f"Test output: {test_vals}")
    test_vals = part_2(test_4_lines)
    print(f"Test output: {test_vals}")
    test_vals = part_2(test_5_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")