import re
from functools import reduce 

num_cubes_in_bag = (12, 13, 14)

def get_game_id(line: str):
    game_id_str, _ = line.split(":")
    game_id = int(re.findall(r"\d+", game_id_str)[0])
    return game_id

def valid_game(num_cubes, line: str):
    _, game_record_str = line.split(":")
    game_records = game_record_str.split(";")
    for record in game_records:
        rgb = re.findall(r"(\d+) red|(\d+) green|(\d+) blue", record)
        rgb = [list(i) for i in zip(*rgb)]
        rgb = [''.join(x) for x in rgb]
        rgb = [0 if x == '' else int(x) for x in rgb]
    
        # check if the values are valid for each record
        rgb_comparison = [cube >= record for cube, record in zip(num_cubes, rgb)]
        # return valid if all records are valid
        if not(all(rgb_comparison)):
            print(f"Invalid record: {rgb}")
            return False
        
    return True

def minimum_cubes(line: str):
    _, game_record_str = line.split(":")
    game_records = game_record_str.split(";")
    rgb_records = []
    for record in game_records:
        rgb = re.findall(r"(\d+) red|(\d+) green|(\d+) blue", record)
        rgb = [list(i) for i in zip(*rgb)]
        rgb = [''.join(x) for x in rgb]
        rgb = [0 if x == '' else int(x) for x in rgb]

        # find the minimum number of cubes across records
        rgb_records.append(rgb)

    rgb_min = [max(cubes) for cubes in zip(*rgb_records)]
    return rgb_min

    
def part_1(lines):
    # red, green, blue cubes in the bag
    print(f"Number of cubes: {num_cubes_in_bag}")
    total = 0

    for line in lines:
        game_id = get_game_id(line)
        if valid_game(num_cubes_in_bag, line):
            print(f"Game {game_id} valid")
            total += game_id
        else:
            print(f"Game {game_id} invalid")
        
    return total
    
def part_2(lines):
    # red, green, blue cubes in the bag
    total = 0

    for line in lines:
        rgb = minimum_cubes(line)
        power = reduce(lambda x, y: x*y, rgb)
        game_id = get_game_id(line)
        print(f"Game {game_id}: {rgb}, {power}")
        total += power
        
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


