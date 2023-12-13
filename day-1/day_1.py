import re

def calibration_value(line):
    # extract all numbers from the line
    nums = [n for n in line if n.isdigit()]
    # take first and last values
    vals = [nums[0], nums[-1]]
    # convert to an integer
    return int(''.join(vals))

def calibration_value_pt2(line):
    text_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # generate regex pattern
    # need to include lookahead in pattern because findall doesn't include overlapping matches
    pattern = r"(?=(" + "|".join(text_nums) + "|\d))"
    # find all matches
    matches = re.findall(pattern, line)
    print(matches)
    # get the first and last match
    first_match = matches[0]
    last_match = matches[-1]

    # map text numbers to numbers
    for i, word in enumerate(text_nums):
        if first_match == word:
            first_match = str(i+1)
        if last_match == word:
            last_match = str(i+1)

    vals = [first_match, last_match]

    # now compute calibration value as before
    return int(''.join(vals))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    print("Part 1")
    calibration_values = [calibration_value(line) for line in lines]
    total = sum(calibration_values)
    print(f"Sum of calibration values: {total}")

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    print("Part 2")
    calibration_values = [calibration_value_pt2(line) for line in lines]
    print(calibration_values)
    total = sum(calibration_values)
    print(f"Sum of calibration values: {total}")


