from copy import copy, deepcopy
from enum import Enum
from functools import cache
import sys

sys.setrecursionlimit(3000)

class Direction(Enum):
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'

def print_grid(grid):
    grid = deepcopy(grid)
    g = [''.join(row) for row in grid]
    print('\n'.join(g))
    print('============')


class Beam:
    def __init__(self, x, y, direction, caves):
        self.history = [(x, y, direction)]
        # list of active beams
        self.beams = [(x, y, direction)]
        self.caves = caves
        self.num_rows = len(caves)
        self.num_cols = len(caves[0])
        energised = copy(caves)
        self.energised = [list(row) for row in energised]

    def run(self):
        # run all beams to completion
        while len(self.beams) > 0:
            updated_beams = []
            for beam in self.beams:
                updated_beams += self.move(beam)
            
            self.beams = updated_beams
        
        print_grid(self.energised)

    def get_num_energised(self):
        return sum([c == 'X' for r in self.energised for c in r])

    def move(self, beam):

        updated_beams = []
        x, y, direction = beam
        self.energised[y][x] = 'X'
        caves = self.caves
        if caves[y][x] == '.':
            if direction == Direction.RIGHT:
                x += 1
            elif direction == Direction.LEFT:
                x -= 1
            elif direction == Direction.UP:
                y -= 1
            elif direction == Direction.DOWN:
                y += 1

        elif caves[y][x] == '/':
            if direction == Direction.RIGHT:
                direction = Direction.UP
                y -= 1
            elif direction == Direction.LEFT:
                direction = Direction.DOWN
                y += 1
            elif direction == Direction.UP:
                direction = Direction.RIGHT
                x += 1
            elif direction == Direction.DOWN:
                direction = Direction.LEFT
                x -= 1

        elif caves[y][x] == '\\':
            if direction == Direction.RIGHT:
                direction = Direction.DOWN
                y += 1
            elif direction == Direction.LEFT:
                direction = Direction.UP
                y -= 1
            elif direction == Direction.UP:
                direction = Direction.LEFT
                x -= 1
            elif direction == Direction.DOWN:
                direction = Direction.RIGHT
                x += 1

        elif caves[y][x] == '-':
            if direction == Direction.RIGHT:
                x += 1
            elif direction == Direction.LEFT:
                x -= 1
            elif direction == Direction.UP or direction == Direction.DOWN:
                updated_beams.append((x-1, y, direction.LEFT))
                x += 1
                direction = Direction.RIGHT
        elif caves[y][x] == '|':
            if direction == Direction.UP:
                y -= 1
            elif direction == Direction.DOWN:
                y += 1
            elif direction == Direction.LEFT or direction == Direction.RIGHT:
                updated_beams.append((x, y-1, direction.UP))
                direction = Direction.DOWN
                y += 1
        
        updated_beams.append((x, y, direction))
        for beam in updated_beams:
            x, y, direction = beam
            if self.out_of_bounds(x, y):
                updated_beams.remove(beam)
            elif self.in_cycle(x, y, direction):
                updated_beams.remove(beam)
            else:
                self.history.append((x, y, direction))
        
        return updated_beams

    def out_of_bounds(self, x, y):
        return x < 0 or x >= self.num_cols or y < 0 or y >= self.num_rows

    def in_cycle(self, x, y, direction):
        return (x, y, direction) in self.history

    def __str__(self):
        return f"({self.x}, {self.y}, {self.direction}, {self.beam_id})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.direction}, {self.beam_id})"



def part_1(lines):
    # parse input
    caves = [line.strip('\n') for line in lines]
    num_rows = len(caves)
    num_cols = len(caves[0])
    print(f"num_rows: {num_rows}, num_cols: {num_cols}")
    # set up start position - each beam is defined by a 4-tuple of x coord, y coord, direction, and beam id
    beam = Beam(0, 0, Direction.RIGHT, caves)
    beam.run()
    return beam.get_num_energised()
    
    
def part_2(lines):
    caves = [line.strip('\n') for line in lines]
    num_cols = len(caves[0])
    num_rows = len(caves)
    history = []
    energised_dict = {}

    def out_of_bounds(x, y):
        #print(f"out_of_bounds: {x}, {y}")
        out_of_bounds = x < 0 or x >= num_cols or y < 0 or y >= num_rows
        #if out_of_bounds:
        #    print(f"num_cols: {num_cols}, num_rows: {num_rows}")
        #    print(f"out_of_bounds: {x}, {y}")
        return out_of_bounds

    def move(x, y, direction):
        #print(f"move: {x}, {y}, {direction}")
        def in_cycle(x, y, direction):
            return (x, y, direction) in history
        
        updated_beams = []
        if caves[y][x] == '.':
            if direction == Direction.RIGHT:
                x += 1
            elif direction == Direction.LEFT:
                x -= 1
            elif direction == Direction.UP:
                y -= 1
            elif direction == Direction.DOWN:
                y += 1

        elif caves[y][x] == '/':
            if direction == Direction.RIGHT:
                direction = Direction.UP
                y -= 1
            elif direction == Direction.LEFT:
                direction = Direction.DOWN
                y += 1
            elif direction == Direction.UP:
                direction = Direction.RIGHT
                x += 1
            elif direction == Direction.DOWN:
                direction = Direction.LEFT
                x -= 1

        elif caves[y][x] == '\\':
            if direction == Direction.RIGHT:
                direction = Direction.DOWN
                y += 1
            elif direction == Direction.LEFT:
                direction = Direction.UP
                y -= 1
            elif direction == Direction.UP:
                direction = Direction.LEFT
                x -= 1
            elif direction == Direction.DOWN:
                direction = Direction.RIGHT
                x += 1

        elif caves[y][x] == '-':
            if direction == Direction.RIGHT:
                x += 1
            elif direction == Direction.LEFT:
                x -= 1
            elif direction == Direction.UP or direction == Direction.DOWN:
                updated_beams.append((x-1, y, direction.LEFT))
                x += 1
                direction = Direction.RIGHT
        elif caves[y][x] == '|':
            if direction == Direction.UP:
                y -= 1
            elif direction == Direction.DOWN:
                y += 1
            elif direction == Direction.LEFT or direction == Direction.RIGHT:
                updated_beams.append((x, y-1, direction.UP))
                direction = Direction.DOWN
                y += 1
        
        updated_beams.append((x, y, direction))
        #print(f"updated_beams: {updated_beams}")
        beams = copy(updated_beams)
        for beam in beams:
            x, y, direction = beam
            if out_of_bounds(x, y):
                #print(f"out of bounds: {x}, {y}, {direction}")
                updated_beams.remove(beam)
            elif in_cycle(x, y, direction):
                updated_beams.remove(beam)
            else:
                history.append((x, y, direction))
        
        return updated_beams

    def get_energised(x, y, direction):
        #print(f"get_energised: {x}, {y}, {direction}")
        if (x, y, direction) in energised_dict.keys():
            print(f"energised_dict {x}, {y}, {direction}: {energised_dict[(x, y, direction)]}")
            return energised_dict[(x, y, direction)]
        
        new_beams = move(x, y, direction)
        #print(f"new_beams: {new_beams}")
        energised = set([(x, y, direction)])
        for beam in new_beams:
            x, y, direction = beam
            # add elements of set to set
            energised |= get_energised(x, y, direction)
        
        energised_dict[(x, y, direction)] = energised
        #print(energised_dict)
        return energised

    # scan boundary cells 
    # generate list of boundary cells
    boundary_cells = [(x, 0, Direction.DOWN) for x in range(num_cols)]
    boundary_cells += [(x, num_rows-1, Direction.UP) for x in range(num_cols)]
    boundary_cells += [(0, y, Direction.RIGHT) for y in range(num_rows)]
    boundary_cells += [(num_cols-1, y, Direction.LEFT) for y in range(num_rows)]
    #boundary_cells = [(0, 0, Direction.RIGHT), (3, 0, Direction.DOWN)]
    print(f"boundary_cells: {boundary_cells}, num_cells = {len(boundary_cells)}")

    # loop over boundary cells and get energised set
    #energised = [get_energised(x, y, direction) for x, y, direction in boundary_cells]
    energised = []
    for i, (x, y, direction) in enumerate(boundary_cells):
        print(i)
        #print(f"boundary cell: {x}, {y}, {direction}")
        history = []
        energised_dict = {}
        e = get_energised(x, y, direction)
        e_set = set((x, y) for x, y, _ in e)

        #print(f"energised: {e}")
        #print(f"num_energised: {len(e_set)}")
        energised.append(e_set)
    # get number of energised cells for each boundary cell
    num_energised = [len(e) for e in energised]
    print(f"num_energised: {num_energised}")
    # determine the maximum
    max_energised = max(num_energised)

    return max_energised
        

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    #print("Part 1 ======================")
    #test_vals = part_1(test_lines)
    #print(f"Test output: {test_vals}")
    input_vals = part_1(input_lines)
    print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")