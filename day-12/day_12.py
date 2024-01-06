import re

        
def is_valid_record(record, contig):
    # if record contains unknown character return False
    if '?' in record:
        return False

    # find all groups of '#'s in record
    matches = re.findall(r'#+', record)
    # get lengths of each group 
    lengths = [len(match) for match in matches]
    # check if lengths matches contig
    return lengths == contig
    

def part_1(lines):
    records = []
    # parse input
    for line in lines:
        record, contig_groups = line.split()
        contig_groups = contig_groups.split(',')
        contig_groups = [int(c) for c in contig_groups]
        records.append((record, contig_groups))

    # process records
    num_records_possible = []
    for record, contig_groups in records:
        def check_record(pos, group):
            #print(f"check_record({pos}, {group})")
            num_ways=0

            if pos == len(record):
                return 1 if group == len(contig_groups) else 0
            
            if record[pos] in '.?':
                # treat as non-defective either way (i.e. as a '.')
                num_ways += check_record(pos+1, group)
            
            if group >= len(contig_groups):
                return num_ways

            end_index = pos + contig_groups[group]

            # now see if we can form a contiguous group of #
            if end_index >= len(record):
                return num_ways
            
            if '.' not in record[pos:end_index] and record[end_index] != '#':
                num_ways += check_record(end_index + 1, group+1)

            #print(num_ways)
            return num_ways

        # append ? to end of record 
        record += '?'
        print(f"Processing record: {record} {contig_groups}")
        num_ways = check_record(0, 0)
        print(f"Num ways: {num_ways}")
        num_records_possible.append(num_ways)


    return sum(num_records_possible)
    
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
    #print(is_valid_record('#.#.###', [1,1,3])
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    # print("Part 2 ======================")
    # test_vals = part_2(test_lines)
    # print(f"Test output: {test_vals}")
    # input_vals = part_2(input_lines)
    # print(f"Real output: {input_vals}")