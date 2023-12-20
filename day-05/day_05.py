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
    
    def map_range(self, low, high):
        # check if the input range is contained in any of the map ranges
        mapped_ranges = []
        for dest, source, range_length in self.ranges:
            # case 2: input range is contained in a single map range - return the mapped values of low/high from the corresponding range
            if low >= source and high < source + range_length:
                mapped_ranges.append((low - source + dest, high - source + dest))
                break
            # case 3: input range is contained in multiple map ranges - return each mapped range
            elif low < source and high >= source + range_length:
                mapped_ranges.append((dest, dest + range_length - 1))
                low = source + range_length
            elif low < source and source < high < source + range_length: 
                mapped_ranges.append((dest, high - source + dest))
                high = source
        
        # case 1: no corresponding map range - return identity
        if len(mapped_ranges) == 0:
            mapped_ranges=[(low, high)]

        return mapped_ranges
    
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
    # extract seeds
    seeds = re.findall('(\d+) (\d+)', lines[0])
    seeds = [(int(s), int(r)) for s, r in seeds]

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
    min_val = None
    for low_seed, range_length in seeds:
        print(f"Seed: {low_seed}, {range_length}")
        high_seed = low_seed + range_length - 1
        ranges = [(low_seed, high_seed)]
        for seed_map in maps:
            new_ranges = []
            # map each range
            for low, high in ranges:
                new_ranges += seed_map.map_range(low, high)
            
            ranges = new_ranges
            #print(f"Ranges: {ranges}")
        
        min_loc = min([low for low, _ in ranges])
        locations.append(min_loc)
        print(ranges)
        
        #locations.append(seed_range_locs)

    print(f"(Seed, location): {list(zip(seeds, locations))}")
    # find the minimum location value
    return min(locations)

    

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