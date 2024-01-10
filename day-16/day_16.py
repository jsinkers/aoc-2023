from enum import Enum

class Direction(Enum):
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'


def part_1(lines):
    # parse input
    caves = [line.strip('\n') for line in lines]
    num_rows = len(caves)
    num_cols = len(caves[0])
    print(f"num_rows: {num_rows}, num_cols: {num_cols}")
    energised = [[[] for _ in range(num_cols)] for _ in range(num_rows)]
    # set up start position - each beam is defined by a 4-tuple of x coord, y coord, direction, and beam id
    latest_beam_id = 0
    beams = [(0, 0, Direction.RIGHT, latest_beam_id)]

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
    
    while len(beams) > 0:
        # update position of each beam
        new_beams = []
        for beam in beams:
            x, y, direction, beam_id = beam
            # mark as energised 
            energised[y][x] += [beam_id]
            print_energised()
            
            if caves[y][x] == '.':
                if direction == Direction.RIGHT:
                    x += 1
                elif direction == Direction.LEFT:
                    x -= 1
                elif direction == Direction.UP:
                    y -= 1
                elif direction == Direction.DOWN:
                    y += 1

                new_beams.append((x, y, direction, beam_id))
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

                new_beams.append((x, y, direction, beam_id))
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

                new_beams.append((x, y, direction, beam_id))
            elif caves[y][x] == '-':
                if direction == Direction.RIGHT:
                    x += 1
                    new_beams.append((x, y, direction, beam_id))
                elif direction == Direction.LEFT:
                    x -= 1
                    new_beams.append((x, y, direction, beam_id))
                elif direction == Direction.UP:
                    new_beams.append((x-1, y, direction.LEFT, beam_id))
                    latest_beam_id += 1
                    new_beams.append((x+1, y, direction.RIGHT, latest_beam_id))
                elif direction == Direction.DOWN:
                    new_beams.append((x-1, y, direction.LEFT, beam_id))
                    latest_beam_id += 1
                    new_beams.append((x+1, y, direction.RIGHT, latest_beam_id))
            elif caves[y][x] == '|':
                if direction == Direction.UP:
                    y -= 1
                    new_beams.append((x, y, direction, beam_id))
                elif direction == Direction.DOWN:
                    y += 1
                    new_beams.append((x, y, direction, beam_id))
                elif direction == Direction.LEFT:
                    new_beams.append((x, y-1, direction.UP, beam_id))
                    latest_beam_id += 1
                    new_beams.append((x, y+1, direction.DOWN, latest_beam_id))
                elif direction == Direction.RIGHT:
                    new_beams.append((x, y-1, direction.UP, beam_id))
                    latest_beam_id += 1
                    new_beams.append((x, y+1, direction.DOWN, latest_beam_id))

            # check if beams have left grid
            # if so, remove them from the list
            beams = new_beams
            for beam in beams:
                try:
                    x, y, direction, beam_id = beam
                except ValueError:
                    print(beam)
                if x < 0 or x >= num_cols or y < 0 or y >= num_rows:
                    beams.remove(beam)
                elif beam_id in energised[y][x]:
                    beams.remove(beam)
        

    return num_energised
    
    
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