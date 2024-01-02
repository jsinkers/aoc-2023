import re

def next_history_val(inp):
    # compute the differences between values
    diffs = [inp[i+1] - inp[i] for i in range(len(inp)-1)]
    # recursively generate next value
    # base case: if all diffs are 0
    if all([d == 0 for d in diffs]):
        return inp[-1]

    # recursive case: compute next value
    return inp[-1] + next_history_val(diffs)




def part_1(lines):
    vals = []
    for line in lines:
        nums = line.split(' ')
        nums = [int(num) for num in nums]
        val = next_history_val(nums)
        vals.append(val)
        
    print(vals)
    return sum(vals)
    
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