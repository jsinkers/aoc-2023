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
    
def part_2(lines, scale_factor):
    print(f"scale_factor={scale_factor}")
    # parse input
    data = []
    empty_rows = []
    for i, line in enumerate(lines):
        new_data = list(line.strip())
        data.append(new_data)
        # expand space along rows
        if all([d == '.' for d in new_data]):
            empty_rows.append(i)
    
    # expand space along columns
    data = list(zip(*data))
    empty_cols = []
    for i, row in enumerate(data):
        if all([d == '.' for d in row]):
            empty_cols.append(i)

    print(f"Empty rows: {empty_rows}")
    print(f"Empty cols: {empty_cols}")
    # transpose back to row/column format
    data = list(zip(*data))
    #print_grid(data)

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
            # determine space expansion
            er = [r for r in empty_rows if min(pos1[0], pos2[0]) < r < max(pos1[0], pos2[0])]
            ec = [c for c in empty_cols if min(pos1[1], pos2[1]) < c < max(pos1[1], pos2[1])]

            num_empty_rows = len(er)
            num_empty_cols = len(ec)
            num_empty = num_empty_cols + num_empty_rows
            
            adjusted_dist = dist + (scale_factor - 1)*num_empty
            #print(f"Pos1: {pos1}, Pos2: {pos2}, Empty rows: {er}, Empty cols: {ec}, Dist: {dist}, Adjusted_dist: {adjusted_dist}")
            distances.append(adjusted_dist)

    # return sum of distances
    #print(f"Distances: {distances}")
    return sum(distances)

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    #input_vals = part_1(input_lines)
    #print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines, scale_factor=2)
    print(f"Test output: {test_vals}")
    test_vals = part_2(test_lines, scale_factor=10)
    print(f"Test output: {test_vals}")
    test_vals = part_2(test_lines, scale_factor=100)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines, scale_factor=1000000)
    print(f"Real output: {input_vals}")