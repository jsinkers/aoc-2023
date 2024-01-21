from copy import deepcopy
import re

def print_grid(grid):
    grid = deepcopy(grid)
    g = [''.join(row) for row in grid]
    print('\n'.join(g))
    print('============')
        

def part_1(lines, num_steps=64):
    garden = []
    for i, line in enumerate(lines):
        line = line.strip()
        garden.append(list(line))
        if 'S' in line:
            start = (i, line.index('S'))
    
    num_rows = len(garden)
    num_cols = len(garden[0])

    def out_of_bounds(x, y):
        return x < 0 or x >= num_cols or y < 0 or y >= num_rows

    def print_garden(positions):
        grid = deepcopy(garden) 
        for x, y in positions:
            grid[y][x] = 'O'
        print_grid(grid)

    current_positions = set([start])
    for i in range(num_steps):
        new_positions = set()
        for position in current_positions:
            x, y = position
            # try to move up, down, left, right
            candidate_posns = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for x, y in candidate_posns:
                if out_of_bounds(x, y):
                    continue
                else:
                    if garden[y][x] in '.S':
                        new_positions.add((x, y))
            
        current_positions = new_positions

    print(f"Step {i+1}: num positions={len(current_positions)}")
    print_garden(current_positions)
   
    return len(current_positions) 

def part_2(lines, num_steps=26501365):
    garden = []
    for i, line in enumerate(lines):
        line = line.strip()
        garden.append(list(line))
        if 'S' in line:
            start = (i, line.index('S'))
    
    num_rows = len(garden)
    num_cols = len(garden[0])

    def print_garden(positions):
        grid = deepcopy(garden) 
        for x, y in positions:
            grid[y][x] = 'O'
        print_grid(grid)

    visited = set()
    frontier = set([start])
    for i in range(num_steps):
        new_frontier = set()
        for x, y in frontier:
            #x, y = frontier.pop()
            visited.add((x, y))
            # try to move up, down, left, right
            candidate_posns = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for x, y in candidate_posns:
                if garden[y % num_rows][x % num_cols] in '.S':
                    if (x, y) not in visited:
                        new_frontier.add((x, y))
            
        frontier = new_frontier
        #print(f"Num visited={len(visited)}")
        print(f"Step {i+1}: frontier posns={len(frontier)}")

    #print_garden(current_positions)
   
    return len(visited) 
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines, num_steps=6)
    print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    #print("Part 2 ======================")
    test_vals = part_2(test_lines, num_steps=6)
    print(f"Test output: {test_vals}")
    #input_vals = part_2(input_lines)
    #print(f"Real output: {input_vals}")