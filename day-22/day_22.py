import re
from copy import deepcopy
import heapq


def part_1(lines):
    # parse input
    bricks = []
    heapq.heapify(bricks)

    max_x, max_y, max_z = 0, 0, 0
    for line in lines:
        coords = line.split('~')
        coords1 = [int(x) for x in coords[0].split(',')]
        coords2 = [int(x) for x in coords[1].split(',')]
        min_z = min(coords1[2], coords2[2])
        # insert brick using min_z as priority
        heapq.heappush(bricks, (min_z, coords1, coords2))
        #bricks.append((coords1, coords2))
        max_x = max(max_x, coords1[0], coords2[0])
        max_y = max(max_y, coords1[1], coords2[1])
        max_z = max(max_z, coords1[2], coords2[2])
    
    # now move bricks down until they hit the floor or another brick
    # make an xy grid the size of max_x, max_y, initially on the floor
    height_envelope = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    # this will act as an envelope of the top of all already moved bricks
    moved_bricks = []
    for i in range(len(bricks)):
        min_z, coords1, coords2 = heapq.heappop(bricks)
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
        diff = min_z - envelope_max - 1
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


    def print_grid(direction):
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
            label = chr(ord('A') + i)  # generate label
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

    #print(moved_bricks)
    print_grid('xz')
    print_grid('yz')

    # now see if the brick is safe to disintegrate - i.e. is not supporting any bricks directly above it
    for i, brick in enumerate(moved_bricks):
        coords1, coords2 = brick
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        # brick_envelope
        supporting = False
        if i == len(moved_bricks) - 1:
            continue

        for j, brick2 in enumerate(moved_bricks[i+1:]):
            coords3, coords4 = brick2
            x3, y3, z3 = coords3
            x4, y4, z4 = coords4
            # check if brick2 is directly above brick
            if z3 == z2:
                # at same height
                continue
            elif z3 > z2 + 1:
                # we're now higher up - no more bricks to check
                # no brick found
                break
            elif z3 == z2 + 1:
                # is there overlap in x and y?
                for x in range(x3, x4+1):
                    for y in range(y3, y4+1):
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            supporting = True
                            break
                    if supporting:
                        break
        
        if not supporting:
            print(f"Brick {i} is safe to disintegrate")

        else:
            print(f"Brick {i} is NOT safe to disintegrate")
        
    total = 0
    return total
    
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
    #input_vals = part_1(input_lines)
    #print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")