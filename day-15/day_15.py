import re

        
def HASH(inp_str):
    val = 0
    for c in inp_str:
        val += ord(c) 
        val *= 17
        val %= 256
    
    return val

def part_1(lines):
    line = lines[0].split(',')
    hash_vals = [HASH(inp) for inp in line]
    print(list(zip(line, hash_vals)))
    return sum(hash_vals)

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