from copy import deepcopy
import re
import heapq
        
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
    queue = [(0, [(0, 0)])]
    heapq.heapify(queue)
    finished_paths = []

    def get_straight_line_steps(path):
        if len(path) == 0:
            return 0
        else:
            x, y = path[-1]
            ind = len(path) - 2
            num_steps = 0
            # case 2: we're moving left or right
            if x == path[ind][0]:
                while ind >= 0 and x == path[ind][0]:
                    num_steps += 1
                    ind -= 1
                
            # case 1: we're moving up or down
            elif y == path[ind][1]:
                while ind >= 0 and y == path[ind][1]:
                    num_steps += 1
                    ind -= 1

            return num_steps
    
    def visited(x, y, path):
        for x1, y1 in path[:-1]:
            if x == x1 and y == y1:
                return True
        return False
    
    def out_of_bounds(x, y):
        return x < 0 or x >= num_cols or y < 0 or y >= num_rows
    
    def exceeded_straight_line_steps(path):
        return get_straight_line_steps(path) > max_straight_line_steps

    explored = set()

    while len(queue) > 0:
        current_location = heapq.heappop(queue)
        heat_loss, path = current_location
        print(heat_loss)
        x, y = path[-1]

        # check if we've reached the end
        if x == end_location[0] and y == end_location[1]:
            print(f"Found path: {path}, heat loss: {heat_loss}")
            finished_path = path
            break

        # move in different directions
        explored.add((x, y))
        new_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for new_x, new_y in new_positions:
            if (new_x, new_y) in explored:
                print(f"explored {new_x}, {new_y}")
                continue
            if out_of_bounds(new_x, new_y) or visited(new_x, new_y, path) or exceeded_straight_line_steps(path + [(new_x, new_y)]):
                continue
            else:
                # insert new state into queue based on current heat loss
                new_heat_loss = heat_loss + heat_loss_map[y][x]
                heapq.heappush(queue, (new_heat_loss, path + [(new_x, new_y)]))

    path_map = deepcopy(heat_loss_map)
    min_heat_loss = 0
    for path in finished_path:
        x, y = path
        if x == 0 and y == 0:
            continue
        min_heat_loss += heat_loss_map[y][x]
        path_map[y][x] = '.'
        
    
    for row in path_map:
        row = [str(x) for x in row]
        print(''.join(row))

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