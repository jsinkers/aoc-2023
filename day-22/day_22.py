import re
from copy import deepcopy
import heapq


def part_1(lines, convert=True):
    # parse input
    bricks = []
    #heapq.heapify(bricks)

    max_x, max_y, max_z = 0, 0, 0
    for line in lines:
        coords = line.split('~')
        coords1 = [int(x) for x in coords[0].split(',')]
        coords2 = [int(x) for x in coords[1].split(',')]
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        z1, z2 = min(z1, z2), max(z1, z2)
        coords1 = (x1, y1, z1)
        coords2 = (x2, y2, z2)
        # insert brick using min_z as priority
        #heapq.heappush(bricks, (z1, coords1, coords2))
        bricks.append((coords1, coords2))
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
        max_z = max(max_z, z1, z2)
    
    # sort bricks by z 
    bricks.sort(key=lambda x: x[0][2])
    # now move bricks down until they hit the floor or another brick
    # make an xy grid the size of max_x, max_y, initially on the floor
    height_envelope = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    # this will act as an envelope of the top of all already moved bricks
    moved_bricks = []
    for i in range(len(bricks)):
        #min_z, coords1, coords2 = heapq.heappop(bricks)
        coords1, coords2 = bricks.pop(0)
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        #print(f"Brick {i}: {coords1} ~ {coords2}")
        #print(height_envelope)
        # look at the max of the envelope restricted to the x, y coords of the brick
        envelope_max = 0
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                envelope_max = max(envelope_max, height_envelope[y][x])

        # move the brick down to that height + 1
        diff = z1 - envelope_max - 1
        #print(diff)
        z1 -= diff
        z2 -= diff

        # reset the envelope to account for the brick
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                #print(f"{x}, {y}")
                height_envelope[y][x] = max(z1, z2, height_envelope[y][x])
        
        # add the brick to the moved bricks
        moved_bricks.append(((x1, y1, z1), (x2, y2, z2)))


    def print_grid(direction, convert=True):
        # generate grid
        print(direction)
        if direction == 'xz':
            max_d = max_x
        elif direction == 'yz':
            max_d = max_y

        grid = [['.' for _ in range(max_d+1)] for _ in range(max_z+1)]
        # fill in bricks
        for i, brick in enumerate(moved_bricks):
            # assign a single character label to each brick
            if convert:
                label = chr(ord('A') + i)  # generate label
            else:
                label = 'x'
            coords1, coords2 = brick
            x1, y1, z1 = coords1
            x2, y2, z2 = coords2
            if direction == 'xz':
                d1 = x1
                d2 = x2
            elif direction == 'yz':
                d1 = y1
                d2 = y2
            else:
                raise ValueError(f"Invalid direction: {direction}")

            for d in range(d1, d2+1):
                for z in range(z1, z2+1):
                    grid[z][d] = label

        # reverse grid
        grid = grid[::-1]
        # label bricks
        g = [''.join(row) for row in grid]
        print('\n'.join(g))
        print('============')

    #print_grid('xz', convert)
    #print_grid('yz', convert)

    # now see if the brick is safe to disintegrate - i.e. is not supporting any bricks directly above it
    # supported_by is a lookup of all bricks that a given brick is supported by
    supported_by = [[] for _ in range(len(moved_bricks))]
    # supporting_list is a lookup of all bricks that a given brick is supporting
    supporting_list = [[] for _ in range(len(moved_bricks))]
    for i, brick in enumerate(moved_bricks):
        coords1, coords2 = brick
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        supporting = False
        if i == len(moved_bricks) - 1:
            continue

        for j, brick2 in enumerate(moved_bricks[i+1:]):
            ind = i + j + 1
            #print(f"checking brick {i} against brick {ind}")
            coords3, coords4 = brick2
            x3, y3, z3 = coords3
            x4, y4, _  = coords4
            # check if brick2 is directly above brick
            if z3 == z2 + 1:
                # is there overlap in x and y?
                for x in range(x3, x4+1):
                    for y in range(y3, y4+1):
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            supporting = True
                            break
                    if supporting:
                        break

            if supporting:
                #print(f"brick {i} supports brick {ind}")
                supported_by[ind].append(i)
                supporting_list[i].append(ind)
                supporting = False
            
    # now determine if safe to disintegrate
    def safe_to_disintegrate(brick):
        # safe to disintegrate if all bricks it supports are supported by more than one brick
        for supported in supporting_list[brick]:
            if len(supported_by[supported]) <= 1:
                return False

        return True

    #supporting_list = [set(s) for s in supporting_list]
    #supported_by = [set(s) for s in supported_by]

    num_to_disintegrate = 0
    for i in range(len(moved_bricks)):
        label = chr(ord('A') + i)  # generate label
        bricks = [chr(ord('A') + b) for b in supporting_list[i]]
        bricks2 = [chr(ord('A') + b) for b in supported_by[i]]
        #print(f"{label}: supports {bricks}, supported_by {bricks2}")
        if safe_to_disintegrate(i):
            #print(f"Brick {label} is safe to disintegrate")
            num_to_disintegrate += 1

    return num_to_disintegrate
    
def part_2(lines):
    total = 0
    return total
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('test_2.txt', 'r') as f:
        test_2_lines = f.readlines()

    with open('test_3.txt', 'r') as f:
        test_3_lines = f.readlines()

    with open('test_4.txt', 'r') as f:
        test_4_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    #print("Part 1 ======================")
    #test_vals = part_1(test_lines)
    #print(f"Test output: {test_vals}")
    #test_vals = part_1(test_2_lines)
    #print(f"Test output: {test_vals}")
    #test_vals = part_1(test_3_lines)
    #print(f"Test output: {test_vals}")
    #test_vals = part_1(test_4_lines)
    #print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    # print("Part 2 ======================")
    # test_vals = part_2(test_lines)
    # print(f"Test output: {test_vals}")
    # input_vals = part_2(input_lines)
    # print(f"Real output: {input_vals}")