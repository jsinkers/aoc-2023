import re

class SeedMap:
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2
        self.ranges = []

    def add_range(self, dest, source, range_length):
        self.ranges.append((dest, source, range_length))
    
    def map_value(self, value):
        for dest, source, range_length in self.ranges:
            if value >= source and value < source + range_length:
                return value - source + dest
        # if no map found, return the same value
        return value
    
    def __repr__(self):
        return f"Map from {self.cat1} to {self.cat2} with {len(self.ranges)} ranges"

def part_1(lines):
    # extract seeds
    seeds = re.findall('\d+', lines[0])
    seeds = [int(s) for s in seeds]
    print(f"Seeds: {seeds}")
    maps = []
    new_map = None

    # read in the data
    for line in lines[1:]:
        if ":" in line:
            matches = re.search('(\w+)-to-(\w+)', line)
            cat1 = matches.group(1)
            cat2 = matches.group(2)
            # new map
            new_map = SeedMap(cat1, cat2)
        elif line == "\n":
            # end of map
            if new_map:
                maps.append(new_map)
        else:
            dest, source, range_length = re.findall('\d+', line)
            dest_low = int(dest)
            source_low = int(source)
            range_length = int(range_length)
            new_map.add_range(dest_low, source_low, range_length)
            
    maps.append(new_map)
    print(maps)

    # now for each seed, determine the corresponding location numbers
    locations = []
    for seed in seeds:
        value = seed
        vals = []
        for seed_map in maps:
            #print(f"Mapping {value} with {seed_map}")
            value = seed_map.map_value(value)
            vals.append(value)

        #print(f"Seed {seed} maps to {vals}")
        locations.append(value)

    print(f"(Seed, location): {list(zip(seeds, locations))}")
    # find the minimum location value
    min_location = min(locations)
    return min_location
    
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