import re

# symbols: list per line of [(symbol, position)]
# position: tuple of (start, end) of number
# line number
def is_part_number(line, position, symbols):
    start, end = position
    
    # get symbols on the line before, same line, and line after
    symbols_before = symbols[line-1] if line > 0 else []
    symbols_current = symbols[line]
    symbols_after = symbols[line+1] if line < len(symbols) - 1 else []

    symbols_to_check = symbols_before + symbols_current + symbols_after

    # check whether each symbol is adjacent
    for symbol, position in symbols_to_check:
        if start - 1 <= position <= end:
            return True
    
    return False
        
def get_gear_ratio(line, position, candidate_part_nums):
    gear_ratio = 0
    # get part nums on the line before, current line, and the line after
    can_part_nums_before = candidate_part_nums[line-1] if line > 0 else []
    can_part_nums_current = candidate_part_nums[line]
    can_part_nums_after = candidate_part_nums[line+1] if line < len(candidate_part_nums) - 1 else []
    part_nums_to_check = can_part_nums_before + can_part_nums_current + can_part_nums_after

    # find all part numbers that are adjacent to this gear symbol
    adj_part_nums = []
    for part_num, part_span in part_nums_to_check:
        start, end = part_span
        if start - 1 <= position <= end:
            adj_part_nums.append(part_num)

    # check if a valid gear: exactly 2 part numbers
    if len(adj_part_nums) == 2:
        gear_ratio = adj_part_nums[0] * adj_part_nums[1]
        #print(f"Valid gear ({line}, {position}): {adj_part_nums[0]}, {adj_part_nums[1]}. Ratio: {gear_ratio}")
    else:
        #print(f"Invalid gear ({line}, {position}): {part_nums[0]}, {part_nums[1]}. Ratio: {gear_ratio}")
        pass

    return gear_ratio

def part_1(lines):
    total = 0
    candidate_part_nums = []
    symbols = []
    # extract all numbers from lines
    for line in lines:
        line = line.strip()
        line_part_nums = []
        for match in re.finditer(r"\d+", line):
            line_part_nums.append((int(match.group()), match.span()))
        
        candidate_part_nums.append(line_part_nums)
    
    # extract all symbols from lines
    for line in lines:
        line_symbols = []
        for match in re.finditer(r"[^\d\.\s]", line):
            line_symbols.append((match.group(), match.span()[0]))
        
        symbols.append(line_symbols)
    
    # extract all unique symbols from line_symbols
    unique_symbols = set([s for line_symbols in symbols for s, _ in line_symbols])
    print(f"Unique symbols: {unique_symbols}")
    
    # check whether each number is a part number and compute the sum
    for line, line_part_nums in enumerate(candidate_part_nums):
        for part_num, position in line_part_nums:
            if is_part_number(line, position, symbols):
                #print(f"Part number {part_num} is valid")
                total += part_num
            else:
                #print(f"Part number {part_num} is invalid")
                pass
        
    return total
    
def part_2(lines):
    total = 0
    candidate_part_nums = []
    symbols = []
    # extract all numbers from lines
    for line in lines:
        line = line.strip()
        line_part_nums = []
        for match in re.finditer(r"\d+", line):
            line_part_nums.append((int(match.group()), match.span()))
        
        candidate_part_nums.append(line_part_nums)
    
    # extract all * symbols from lines
    for line in lines:
        line_symbols = []
        for match in re.finditer(r"\*", line):
            line_symbols.append(match.span()[0])
        
        symbols.append(line_symbols)

    # check whether each symbol is a gear
    for line, line_symbols in enumerate(symbols):
        for position in line_symbols:
            gear_ratio = get_gear_ratio(line, position, candidate_part_nums)
            total += gear_ratio
        
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