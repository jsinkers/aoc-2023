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