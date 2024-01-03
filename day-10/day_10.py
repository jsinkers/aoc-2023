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
    total = 0
    return total
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('test_2.txt', 'r') as f:
        test_2_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    test_vals = part_1(test_2_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    #print("Part 2 ======================")
    #test_vals = part_2(test_lines)
    #print(f"Test output: {test_vals}")
    #input_vals = part_2(input_lines)
    #print(f"Real output: {input_vals}")