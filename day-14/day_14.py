import re
        
def print_grid(grid):
    grid = list(zip(*grid))
    g = [''.join(row) for row in grid]
    print('\n'.join(g))

def part_1(lines):
    # parse input
    rock_positions = []
    for line in lines:
        line = line.strip()
        row = line
        rock_positions.append(row)
        
    # transpose
    rock_positions = list(zip(*rock_positions))
    #print_grid(rock_positions)

    # split by # 
    rock_positions = [''.join(row).split('#') for row in rock_positions]
    #print(rock_positions)

    # move all O rocks to start of list
    rotated_rock_positions = []
    for row in rock_positions:
        new_row = []
        for rock_group in row:
            len_rock_group = len(rock_group)
            num_rocks = rock_group.count('O')
            new_row.append('O'*num_rocks + '.'*(len_rock_group - num_rocks))

        #print(new_row)
        new_row = '#'.join(new_row)
        #print(new_row)
        rotated_rock_positions.append(new_row)
        #print(rotated_rock_positions)
    
    #print_grid(rotated_rock_positions)
    # calculate load for each rock
    # transpose again and reverse
    rotated_rock_positions = reversed(list(zip(*rotated_rock_positions)))
    score = [(i+1, row.count('O')) for i, row in enumerate(rotated_rock_positions)]
    score = sum([i*count for i, count in score])
    return score
    
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

    # print("Part 2 ======================")
    # test_vals = part_2(test_lines)
    # print(f"Test output: {test_vals}")
    # input_vals = part_2(input_lines)
    # print(f"Real output: {input_vals}")