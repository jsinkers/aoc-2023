from copy import copy, deepcopy
from enum import Enum

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
    energised = [[[] for _ in range(num_cols)] for _ in range(num_rows)]
    # set up start position - each beam is defined by a 4-tuple of x coord, y coord, direction, and beam id
    beam = Beam(0, 0, Direction.RIGHT, caves)

    def print_energised():
        num_energised = 0
        for i, row in enumerate(energised):
            row_str = ''
            for j, col in enumerate(row):
                if len(col) >= 1:
                    num_energised += 1
                    row_str += '#'
                else:
                    row_str += caves[i][j]
            print(row_str)

        print()
        return num_energised
    
    beam.run()
    return beam.get_num_energised()
    
    
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