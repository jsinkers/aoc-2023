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
        unmapped_inputs = [(low, high)]
        mapped_ranges = []
        # for each range in the map
        for dest, source, range_length in self.ranges:
            s_low = source
            s_high = source + range_length - 1
            new_unmapped_inputs = []
            # for each range of unmapped inputs
            for i_l, i_h in unmapped_inputs:
                # 1: range not applicable to inputs
                if i_h < s_low or i_l > s_high:
                    new_unmapped_inputs.append((i_l, i_h))
                # 2: inputs wholly contained within inputs
                elif i_l >= s_low and i_h <= s_high:
                    mapped_ranges.append((i_l - source + dest, i_h - source + dest))
                # 3: lower bound of input outside of range, upper bound within range
                elif i_l < s_low and s_low <= i_h <= s_high:
                    mapped_ranges.append((dest, i_h - source + dest))
                    new_unmapped_inputs.append((i_l, s_low - 1))
                # 4: lower bound of input within range, upper bound outside of range
                elif s_low <= i_l <= s_high and i_h > s_high:
                    mapped_ranges.append((i_l - source + dest, dest + range_length - 1))
                    new_unmapped_inputs.append((s_high + 1, i_h))
                # 5: lower bound below range, upper bound above range
                elif i_l < s_low and i_h > s_high:
                    mapped_ranges.append((dest, dest + range_length - 1))
                    new_unmapped_inputs.append((i_l, s_low - 1))
                    new_unmapped_inputs.append((s_high + 1, i_h))

            unmapped_inputs = new_unmapped_inputs

        # 6: add any remaining unmapped inputs using identity
        for i_l, i_h in unmapped_inputs:
            mapped_ranges.append((i_l, i_h))

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