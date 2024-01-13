import re

        
class Direction:
    RIGHT = 'right'
    LEFT = 'left'
    UP = 'up'
    DOWN = 'down'

def part_1(lines):
    # parse input
    heat_loss_map = [[int(x) for x in line.strip()] for line in lines]
    num_rows = len(heat_loss_map)
    num_cols = len(heat_loss_map[0])
    start_location = (0, 0)
    end_location = (num_cols - 1, num_rows - 1)
    
    #, [], 0, 0)
    # state on grid is (path, heat_loss)
    # path is a list of tuples (x, y, direction)
    # heat_loss is the sum of the heat loss of all the tiles in the path
    max_straight_line_steps = 3

    # conduct a breadth first search from the start location to the end location to determine the path with minimal
    # heat loss, without taking more than 3 steps in a straight line
    queue = [([(0, 0, Direction.RIGHT)], 0), ((0,0, Direction.DOWN), 0)]
    finished_paths = []

    def get_straight_line_steps(path):
        if len(path) == 0:
            return 0
        else:
            x, y, direction = path[-1]
            if direction == Direction.RIGHT:
                return 1 + get_straight_line_steps(path[:-1])
            else:
                return 0
    
    def visited(x, y, path):
        for x1, y1, _ in path[:-1]:
            if x == x1 and y == y1:
                return True
        return False
    
    def out_of_bounds(x, y):
        return x < 0 or x >= num_cols or y < 0 or y >= num_rows

    while len(queue) > 0:
        print(len(queue))
        current_location = queue.pop(0)
        path, heat_loss = current_location
        x, y, _ = path[-1]

        # check if we're out of bounds
        if out_of_bounds(x, y):
            #print(f"Out of bounds {x},{y}")
            continue

        heat_loss += heat_loss_map[y][x]
        #print(f"Current location: {x}, {y}, {direction}, heat loss: {heat_loss}")
        min_heat_loss = None

        # check if we've already visited this location
        if visited(x, y, path):
            print(f"Visited {x},{y}")
            continue

        # check if we've already exceeded the known minimum heat loss
        if min_heat_loss is not None and heat_loss > min_heat_loss:
            print(f"Exceeded min heat loss {heat_loss} > {min_heat_loss}")
            continue

        # check if we've taken too many straight line steps
        current_straight_line_steps = get_straight_line_steps(path)
        if current_straight_line_steps > max_straight_line_steps:
            continue
    
        # check if we've reached the end
        if x == end_location[0] and y == end_location[1]:
            print(f"Found path: {path}, heat loss: {heat_loss}")
            finished_paths.append((path, heat_loss))
            if min_heat_loss is None or heat_loss < min_heat_loss:
                min_heat_loss = heat_loss
            continue

        # move in different directions
        new_states = [(path + [(y + 1, x, Direction.DOWN)], heat_loss),
                        (path + [(y - 1, x, Direction.UP)], heat_loss),
                        (path + [(y, x + 1, Direction.RIGHT)], heat_loss),
                        (path + [(y, x - 1, Direction.LEFT)], heat_loss)]
        queue += new_states

    return min_heat_loss
    
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