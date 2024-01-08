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
    line = lines[0].split(',')
    boxes = {k: {} for k in range(256)}
    for inp in line:
        matches = re.match(r'(\w+)([=-])(\d?)', inp)
        label = matches.group(1)
        operation = matches.group(2)
        operation = '-' if '-' in inp else '='
        box_id = HASH(label)
        if operation == '-':
            if label in boxes[box_id].keys():
                boxes[box_id].pop(label)
        elif operation == '=':
            focal_length = int(matches.group(3))
            boxes[box_id][label] = focal_length
        
    print(f"After '{inp}':")
    for k, v in boxes.items():
        if len(v.keys()) > 0:
            print(f"Box {k}: {list(v.items())}")
    
    print()

    total_focus_power = 0
    for box, lenses in boxes.items():
        if len(lenses.keys()) == 0:
            continue

        print(f"Box {box}")
        for i, (lens, focal_length) in enumerate(lenses.items()):
            focus_power = (1+box) * (i+1) * focal_length
            total_focus_power += focus_power
            print(f"Lens: {lens}, Slot: {i + 1}, Focal length: {focal_length}, Focus power: {focus_power}")

    return total_focus_power

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    #print("Part 1 ======================")
    #test_vals = part_1(test_lines)
    #print(f"Test output: {test_vals}")
    #input_vals = part_1(input_lines)
    #print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")