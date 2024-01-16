from copy import deepcopy
import re

def print_grid(grid):
    grid = deepcopy(grid)
    g = [''.join(row) for row in grid]
    print('\n'.join(g))
    print('============')
        

def part_1(lines):
    edges = set([(0, 0)])
    x, y = 0, 0
    min_x, min_y = 0, 0
    max_x, max_y = 0, 0
    for line in lines:
        direction, distance, colour = line.split(' ')
        distance = int(distance)
        if direction == 'R':
            for i in range(distance):
                edges.add((x+i+1, y))

            x += distance
        elif direction == 'L':
            for i in range(distance):
                edges.add((x-i-1, y))

            x -= distance
        if direction == 'U':
            for i in range(distance):
                edges.add((x, y-i-1))

            y -= distance
        elif direction == 'D':
            for i in range(distance):
                edges.add((x, y+i+1))

            y += distance
        
        min_x = x if x < min_x else min_x
        min_y = y if y < min_y else min_y
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
    
    print(f"Min x: {min_x}, max x: {max_x}")
    print(f"Min y: {min_y}, may y: {max_y}")
    grid = [['.' for _ in range(min_x, max_x+1)] for _ in range(min_y-1, max_y+1)]
    for edge in edges:
        x, y = edge
        #print(edge)
        grid[y-min_y][x-min_x] = '#'
    
    
    print_grid(grid)
    num_cells = len(edges)
    for row in grid:
        row = ''.join(row)
        match = re.findall(r'#(\.+)#', row)
        if match:
            cells = sum([len(m) for m in match])
            #print(f"Row: {row}, cells: {cells}")
            num_cells += cells

    return num_cells
    
def part_2(lines):
    total = 0
    return total
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    #print("Part 2 ======================")
    #test_vals = part_2(test_lines)
    #print(f"Test output: {test_vals}")
    #input_vals = part_2(input_lines)
    #print(f"Real output: {input_vals}")