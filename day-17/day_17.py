from copy import deepcopy
import re
import heapq
        
class Direction:
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

def part_1(lines):
    # parse input
    heat_loss_map = [[int(x) for x in line.strip()] for line in lines]
    num_rows = len(heat_loss_map)
    num_cols = len(heat_loss_map[0])
    start_location = (0, 0)
    end_location = (num_cols - 1, num_rows - 1)
    
    # state on grid is (path, heat_loss)
    # path is a list of tuples (x, y, direction)
    # heat_loss is the sum of the heat loss of all the tiles in the path
    max_straight_line_steps = 3

    # conduct a breadth first search from the start location to the end location to determine the path with minimal
    # heat loss, without taking more than 3 steps in a straight line
    queue = [(0, 0, 0, 0, Direction.RIGHT, 0), (0, 0, 0, 0, Direction.DOWN, 0)]
    heapq.heapify(queue)

    def out_of_bounds(x, y):
        return x < 0 or x >= num_cols or y < 0 or y >= num_rows
    
    explored = {}

    i = 0
    while len(queue) > 0:
        current_location = heapq.heappop(queue)
        h, heat_loss, x, y, direction, num_steps = current_location

        if i % 100000 == 0:
            print(f"h: {h}, heat loss: {heat_loss}, x: {x}, y: {y}, direction: {direction}, num_steps: {num_steps}, len(queue): {len(queue)}")
        i += 1

        # check if we've reached the end
        if x == end_location[0] and y == end_location[1]:
            #print(f"Found path: {path}, heat loss: {heat_loss}")
            #finished_path = path
            min_heat_loss = heat_loss
            break 

        # move in different directions
        state = (x, y, direction, num_steps)
        new_positions = [(x + 1, y, Direction.RIGHT), (x - 1, y, Direction.LEFT), 
                         (x, y + 1, Direction.DOWN), (x, y - 1, Direction.UP)]
        # don't reverse
        if direction == Direction.RIGHT:
            new_positions.remove((x - 1, y, Direction.LEFT))
        elif direction == Direction.LEFT:
            new_positions.remove((x + 1, y, Direction.RIGHT))
        elif direction == Direction.UP:
            new_positions.remove((x, y + 1, Direction.DOWN))
        elif direction == Direction.DOWN:
            new_positions.remove((x, y - 1, Direction.UP))

        # add new positions to queue
        for new_x, new_y, new_dir in new_positions:
            if out_of_bounds(new_x, new_y):
                continue

            if new_dir == direction:
                new_num_steps = num_steps + 1
                if new_num_steps > max_straight_line_steps:
                    continue
            else:
                new_num_steps = 1

            if (new_x, new_y, new_dir, new_num_steps) in explored:
                #print(f"Already explored: {new_x}, {new_y}, {new_dir}")
                continue

            # insert new state into queue based on current heat loss
            new_heat_loss = heat_loss + heat_loss_map[new_y][new_x]
            # heuristic: manhattan distance to end + heat loss
            # NB as all tiles have a heat loss >= 1, this is an admissible heuristic, so we are guaranteed
            # an optimal solution
            h = new_heat_loss + (abs(new_x - end_location[0]) + abs(new_y - end_location[1]))
            # push onto priority queue according to min heuristic
            heapq.heappush(queue, (h, new_heat_loss, new_x, new_y, new_dir, new_num_steps))
            state = (new_x, new_y, new_dir, new_num_steps)
            explored[state] = new_heat_loss

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