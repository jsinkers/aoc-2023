import re
import math

def part_1(lines):
    # parse input
    # first line gives directions
    directions = lines[0].strip()

    # use a dict to store the map for easy lookup
    map = {}
    position = 'AAA'
    end = 'ZZZ'
    i = 0
    
    # 3rd line onwards defines map
    for line in lines[2:]:
        match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
        source, left, right = match.groups()
        map[source] = (left, right)

    # follow the directions to get to the destination
    while position != end:
        # move to the next position - wrap around with directions
        direction = directions[i % len(directions)]
        if direction == 'L':
            position = map[position][0]
        elif direction == 'R':
            position = map[position][1]
        
        i += 1
    
    return i
    
def part_2(lines):
    # parse input
    # first line gives directions
    directions = lines[0].strip()
    print(directions)

    # use a dict to store the map for easy lookup
    map = {}
    positions = []
    paths = []
    
    def at_end(position):
        return all([p[2] == 'Z' for p in position])
    i = 0
    
    # 3rd line onwards defines map
    for line in lines[2:]:
        match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
        source, left, right = match.groups()
        map[source] = (left, right)
        if source[2] == 'A':
            positions.append(source)
            paths.append([source])

    path_lengths = []
    # follow each path checking for cycles 
    for j, position in enumerate(positions):
        path = [position]
        cycle_detected = False
        i = 0 
        while not cycle_detected:
            # move to the next position - wrap around with directions
            direction = directions[i % len(directions)]
            if direction == 'L':
                new_posn = map[position][0]
            elif direction == 'R':
                new_posn = map[position][1]
            

            position = new_posn
            if new_posn in path:
                # cycle detected
                print(f"Cycle detected for path {j} after {i} steps")
                path_lengths.append(i)
                cycle_detected = True

            i += 1
            path.append(new_posn)
    
    # determine lowest common multiple of path lengths
    return math.lcm(*path_lengths)
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('test_2.txt', 'r') as f:
        test_2_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    print("Part 1 ======================")
    test_vals = part_1(test_lines)
    print(f"Test output: {test_vals}")
    test_2_vals = part_1(test_2_lines)
    print(f"Test 2 output: {test_2_vals}")
    
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    with open('test_3.txt', 'r') as f:
        test_3_lines = f.readlines()

    test_vals = part_2(test_3_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")