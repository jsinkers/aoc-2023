import re
from copy import deepcopy


def print_grid(grid):
    grid = deepcopy(grid)
    g = [''.join(row) for row in grid]
    print('\n'.join(g))
    print('============')
        
def part_1(lines):
    # parse input
    grid = [list(line.strip()) for line in lines]

    # identify start location
    start = (grid[0].index('.'), 0)

    # identify target location
    target = (grid[-1].index('.'), len(grid) - 1, )
    print(f"Start: {start}, Target: {target}")

    # run bfs to find longest path
    def get_neighbours(x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def out_of_bounds(x, y):
        return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])

    queue = [(start, [])]
    longest = 0
    longest_path = []
    slope_dx = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    while len(queue) > 0:
        #print(f"Queue length: {len(queue)}")
        (x, y), path = queue.pop(0)


        if (x, y) == target:
            if len(path) > longest:
                longest = len(path)
                longest_path = path
                print(f"Longest path: {longest}")

        #print(f"y: {y}, x: {x}, path: {path}")
        if grid[y][x] == '.':
                
            for nx, ny in get_neighbours(x, y):
                if out_of_bounds(nx, ny) or grid[ny][nx] == '#' or (nx, ny) in path:
                    continue
                    
                queue.append(((nx, ny), path + [(nx, ny)]))
            
        elif grid[y][x] in '^<>v':
                dx, dy = slope_dx[grid[y][x]]
                nx, ny = x + dx, y + dy

                if out_of_bounds(nx, ny) or grid[ny][nx] == '#' or (nx, ny) in path:
                    continue

                queue.append(((nx, ny), path + [(nx, ny)]))
    
    for x, y in longest_path:
        grid[y][x] = 'O'

    print_grid(grid)
    return longest
    
def part_2(lines):
    # parse input
    grid = [list(line.strip()) for line in lines]

    # identify start location
    start = (grid[0].index('.'), 0)

    # identify target location
    target = (grid[-1].index('.'), len(grid) - 1, )
    print(f"Start: {start}, Target: {target}")

    # run bfs to find longest path
    def get_neighbours(x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def out_of_bounds(x, y):
        return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])

    queue = [(start, [])]
    longest = 0
    longest_path = []
    slope_dx = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    while len(queue) > 0:
        #print(f"Queue length: {len(queue)}")
        (x, y), path = queue.pop(0)


        if (x, y) == target:
            if len(path) > longest:
                longest = len(path)
                longest_path = path
                print(f"Longest path: {longest}")

        #print(f"y: {y}, x: {x}, path: {path}")
        for nx, ny in get_neighbours(x, y):
            if out_of_bounds(nx, ny) or grid[ny][nx] == '#' or (nx, ny) in path:
                continue
                
            queue.append(((nx, ny), path + [(nx, ny)]))
            
    
    for x, y in longest_path:
        grid[y][x] = 'O'

    print_grid(grid)
    return longest
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    #print("Part 1 ======================")
    #test_vals = part_1(test_lines)
    #print(f"Test output: {test_vals}")
    #input_vals = part_1(input_lines)
    #print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")