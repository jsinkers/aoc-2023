import re
from math import sqrt, ceil, floor

        

def part_1(lines):
    # extract all time values from input
    times = re.findall('\d+', lines[0])
    times = [int(t) for t in times]
    distances = re.findall('\d+', lines[1])
    distances = [int(d) for d in distances]
    # via quadratic formula we can determine that the values for which the distance is greater than 0 are:

    num_wins = 1
    for time, distance in zip(times, distances):
        sqrt_det = sqrt(time**2 - 4*distance)
        low = (time - sqrt_det)/2
        high = (time + sqrt_det)/2
        print(f"Time: {time}, Distance: {distance}, Low: {low}, High: {high}")
        low = floor(low+1) if low > 0 else 0
        high = ceil(high-1) if high > 0 else 0
        num_ways = high - low + 1
        print(f"Time: {time}, Distance: {distance}, Low: {low}, High: {high}, Num ways to win: {num_ways}")
        num_wins *= num_ways

    return num_wins
    
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