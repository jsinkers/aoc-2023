import re

        
def print_grid(grid):
    g = [''.join(row) for row in grid]
    print('\n'.join(g))

def part_1(lines):
    # parse input
    data = []
    for line in lines:
        new_data = list(line.strip())
        data.append(new_data)
        # expand space along rows
        if all([d == '.' for d in new_data]):
            data.append(new_data)
    
    # expand space along columns
    data = list(zip(*data))
    new_data = []
    for i, row in enumerate(data):
        new_data.append(row)
        if all([d == '.' for d in row]):
            new_data.append(row)
    
    # transpose back to row/column format
    data = list(zip(*new_data))
    print(data)
    print_grid(data)

    # extract galaxy positions
    galaxy_positions = []
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if row[j] == '#':
                galaxy_positions.append((i, j))
        
    print(f"Num galaxies: {len(galaxy_positions)}")

    # compute pairwise distances (manhattan distance)
    distances = []
    for i, pos1 in enumerate(galaxy_positions):
        for j, pos2 in enumerate(galaxy_positions):
            # skip if same position or if we've already computed this distance
            if i == j or i > j:
                continue
            dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            distances.append(dist)

    # return sum of distances
    print(f"Distances: {distances}")
    return sum(distances)
    
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