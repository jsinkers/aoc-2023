import re

        

def part_1(lines):
    total = 0
    # extract all numbers from lines
    for line in lines:
        card, nums = line.split(':')
        win_nums, card_nums = nums.split('|')
        pattern = '\d+'

        card_id = int(re.search(pattern, card).group())
        card_nums = set([int(n) for n in re.findall(pattern, card_nums)])
        win_nums = set([int(n) for n in re.findall(pattern, win_nums)])
        num_matches = len(card_nums.intersection(win_nums))
        points = 2**(num_matches-1) if num_matches > 0 else 0
        #print(f"Card {card_id} has {num_matches} matches and {points} points")
        total += points
    
    return total
    
def part_2(lines):
    total = 0
    copies = [1] * len(lines)
    # extract all numbers from lines
    for i, line in enumerate(lines):
        card, nums = line.split(':')
        win_nums, card_nums = nums.split('|')
        pattern = '\d+'

        card_id = int(re.search(pattern, card).group())
        card_nums = set([int(n) for n in re.findall(pattern, card_nums)])
        win_nums = set([int(n) for n in re.findall(pattern, win_nums)])
        num_matches = len(card_nums.intersection(win_nums))
        points = 2**(num_matches-1) if num_matches > 0 else 0
        #print(f"Card {card_id} has {num_matches} matches and {points} points")
        # for each copy of the card, repeat the copies of subsequent cards
        for k in range(copies[i]):
            #print(f"k = {k}")
            # increase the number of copies for the card according to the number of matches
            for j in range(i + 1, i + num_matches + 1):
                #print(j)
                if j < len(copies):
                    copies[j] += 1
                else:
                    break
        
        #print(copies)

    print(copies)
    total = sum(copies)
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