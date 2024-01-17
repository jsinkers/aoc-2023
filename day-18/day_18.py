from copy import deepcopy
import re

def print_grid(grid):
    grid = deepcopy(grid)
    g = [''.join(row) for row in grid]
    print('\n'.join(g))
    print('============')
        

def part_1(lines):
    vertices = []

    x, y = 0, 0
    for line in lines:
        direction, distance, colour = line.split(' ')
        distance = int(distance)
        if direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        if direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance
        
        vertices.append((x, y))
    
    # shoelace method for internal area, also determine path length
    # internal area
    total = 0
    path_length = 0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        x1, y1 = vertices[i]
        x2, y2  = vertices[j]
        path_length += abs(x2-x1) + abs(y2-y1)
        total += (x2-x1)*(y1+y2)

    area = abs(total) / 2
    print(f"Internal area: {area}, Path length: {path_length}")
    picks = area + path_length // 2 + 1
    return picks
        
def part_2(lines):
    vertices = []

    x, y = 0, 0
    for line in lines:
        line = line.strip()
        _, _, colour = line.split(' ')

        # get distance to dig from first 5 digits of RGB code
        # remove parentheses from colour
        colour = colour[1:-1]
        dist_hex = colour[1:6]
        distance = int(dist_hex, 16)

        # determine the direction based on last character of RGB code
        directions = 'RDLU'
        direction = directions[int(colour[6])]
        
        print(f"{colour} = {direction} {distance}")

        if direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        if direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance
        
        vertices.append((x, y))
    
    # shoelace method for internal area, also determine path length
    # internal area
    total = 0
    path_length = 0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        x1, y1 = vertices[i]
        x2, y2  = vertices[j]
        path_length += abs(x2-x1) + abs(y2-y1)
        total += (x2-x1)*(y1+y2)

    area = abs(total) / 2
    print(f"Internal area: {area}, Path length: {path_length}")
    picks = area + path_length // 2 + 1
    return picks
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

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")