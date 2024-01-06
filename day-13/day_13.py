import re

def print_grid(grid):
    g = [''.join(row) for row in grid]
    print('\n'.join(g))

def part_1(lines):
    # parse input
    patterns = []
    pattern = []
    for line in lines:
        line = line.strip()
        if line == '':
            #print(f'New pattern: {pattern}')
            patterns.append(pattern)
            pattern = []
        else:
            row = list(line)
            pattern.append(row)
    
    if len(pattern) > 0:
        patterns.append(pattern)
    print(patterns)
    # find reflections
    row_reflections = []
    col_reflections = []
    for pattern in patterns:
        #print(f"Pattern: {pattern}")
        transposed_pattern = list(zip(*pattern))
        #print(f"Transposed Pattern: {transposed_pattern}")
        print("\nRows - ")
        pattern_row_reflections = get_reflection(pattern)
        # transpose pattern
        print(f"Row reflections: {pattern_row_reflections}\n\n")
        print("\nColumns - ")
        pattern_col_reflections = get_reflection(transposed_pattern)
        print(f"Col reflections: {pattern_col_reflections}\n\n")
        row_reflections += pattern_row_reflections
        col_reflections += pattern_col_reflections

    sum_vert_lines = sum([c + 1 for c in col_reflections])
    sum_horiz_lines = sum([r + 1 for r in row_reflections])
    print(f"Sum vert lines: {sum_vert_lines}")
    print(f"Sum horiz lines: {sum_horiz_lines}")
    score = 100*sum_horiz_lines + sum_vert_lines
    return score
    
def get_reflection(pattern):
    num_rows = len(pattern)
    #print_grid(pattern)
    # check rows for reflections
    reflections = []
    for i in range(0, num_rows-1):
        #print(f"\nLine of symmetry at row {i}")
        for j in range(num_rows):
            row1_ind = i - j
            row2_ind = i + j + 1
            #print(f"Checking rows {row1_ind} and {row2_ind}")
            if row1_ind < 0 or row2_ind >= num_rows:
                #print(f"Reflection detected at rows {i}")
                reflections.append(i)
                break
            
            if pattern[row1_ind] != pattern[row2_ind]:
                #print(f"No match at rows {row1_ind} and {row2_ind}")
                break
        
    return reflections

def get_reflection_2(pattern):
    num_rows = len(pattern)

    for i in range(0, num_rows-1):
        diff = 0
        #print(f"\nLine of symmetry at row {i}")
        match = True
        for j in range(num_rows):
            row1_ind = i - j
            row2_ind = i + j + 1
            #print(f"Checking rows {row1_ind} and {row2_ind}")
            if row1_ind < 0 or row2_ind >= num_rows:
                if diff == 1:
                    return i
                
                break
            
            # compute differences between rows
            diff += sum([r1 != r2 for r1, r2 in zip(pattern[row1_ind], pattern[row2_ind])])
        
    return None

def part_2(lines):
    # parse input
    patterns = []
    pattern = []
    for line in lines:
        line = line.strip()
        if line == '':
            #print(f'New pattern: {pattern}')
            patterns.append(pattern)
            pattern = []
        else:
            row = list(line)
            pattern.append(row)
    
    if len(pattern) > 0:
        patterns.append(pattern)
    # find reflections
    row_reflections = []
    col_reflections = []
    for pattern in patterns:
        transposed_pattern = list(zip(*pattern))
        # now look for alternate axis of symmetry
        new_row_reflection = get_reflection_2(pattern)
        new_col_reflection = get_reflection_2(transposed_pattern)
        if new_row_reflection is not None:
            row_reflections.append(new_row_reflection)
        elif new_col_reflection is not None:
            col_reflections.append(new_col_reflection)

    sum_vert_lines = sum([c + 1 for c in col_reflections])
    sum_horiz_lines = sum([r + 1 for r in row_reflections])
    print(f"Sum vert lines: {sum_vert_lines}")
    print(f"Sum horiz lines: {sum_horiz_lines}")
    score = 100*sum_horiz_lines + sum_vert_lines
    return score
    

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