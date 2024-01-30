import re
from copy import deepcopy
import heapq

def print_grid(grid):
    grid = deepcopy(grid)
    g = [''.join(row) for row in grid]
    print('\n'.join(g))
    print('============')
        
def part_1(lines):
    # parse input
    grid = [list(line.strip()) for line in lines]

    # identify start location
    start = (grid[0].index('.'), 0)

    # identify target location
    target = (grid[-1].index('.'), len(grid) - 1, )
    print(f"Start: {start}, Target: {target}")

    # run bfs to find longest path
    def get_neighbours(x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def out_of_bounds(x, y):
        return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])

    queue = [(start, [])]
    longest = 0
    longest_path = []
    slope_dx = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    while len(queue) > 0:
        #print(f"Queue length: {len(queue)}")
        (x, y), path = queue.pop(0)


        if (x, y) == target:
            if len(path) > longest:
                longest = len(path)
                longest_path = path
                print(f"Longest path: {longest}")

        #print(f"y: {y}, x: {x}, path: {path}")
        if grid[y][x] == '.':
                
            for nx, ny in get_neighbours(x, y):
                if out_of_bounds(nx, ny) or grid[ny][nx] == '#' or (nx, ny) in path:
                    continue
                    
                queue.append(((nx, ny), path + [(nx, ny)]))
            
        elif grid[y][x] in '^<>v':
                dx, dy = slope_dx[grid[y][x]]
                nx, ny = x + dx, y + dy

                if out_of_bounds(nx, ny) or grid[ny][nx] == '#' or (nx, ny) in path:
                    continue

                queue.append(((nx, ny), path + [(nx, ny)]))
    
    for x, y in longest_path:
        grid[y][x] = 'O'

    print_grid(grid)
    return longest
    
def part_2(lines):
    # parse input
    grid = [list(line.strip()) for line in lines]

    # identify start location
    start = (grid[0].index('.'), 0)

    # identify target location
    target = (grid[-1].index('.'), len(grid) - 1, )
    print(f"Start: {start}, Target: {target}")

    # run bfs to find longest path
    def get_neighbours(x, y):
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def out_of_bounds(x, y):
        return x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])

    # convert map to graph
    # each node is a location 
    # each edge is weighted by path_length between each location
    # queue items are (prev node location, current location, current distance from prev node)
    queue = [(start, start, 0, [])]
    expanded = set()
    # graph is a dict of nodes and their neighbours with the distance between them
    graph = {start: []}

    # run bfs on map
    # every time a new node is found, add it to the graph
    while len(queue) > 0:
        node1, current_pos, distance, path = queue.pop(0)
        #print(f"{node1} {current_pos} {distance} {path}")
        x, y = current_pos

        # need to check that node has been expanded from the same direction
        if (node1, current_pos) in expanded:
            continue
        
        expanded.add((node1, current_pos))

        neighbours = []
        for nx, ny in get_neighbours(x, y):
            if out_of_bounds(nx, ny) or grid[ny][nx] == '#' or (nx, ny) in path:
                continue
        
            neighbours.append((nx, ny))
        
        # if there's more than 1 neighbour we have a new node (or if we are at the end)
        if len(neighbours) > 1 or current_pos == target:
            if node1 not in graph.keys():
                graph[node1] = []

            graph[node1].append((current_pos, distance))
            node1 = current_pos
            distance = 1
        else:
            distance += 1
        
        for nx, ny in neighbours:
            queue.append((node1, (nx, ny), distance, path + [current_pos]))

        
        # need to prevent expanding the same node multiple times 
        # for some reason adding this where I would expect it to work seems to cause graph not to be generated correctly

    print(graph)
    # now we have the reduced graph, determine the longest path
    queue = [(0, start, [])]
    paths_to_end = []

    while len(queue) > 0:
        print(f"Queue length: {len(queue)}")
        distance, node, path = queue.pop()
        #print(f"priority: {distance}")

        #print(f"{node}, path: {path}")
        if node not in graph.keys():
            print(f"Node not in graph {node}")
            continue

        for neighbour, step_dist in graph[node]:
            if neighbour in path:
                continue
                
            new_path = path + [neighbour]
            new_dist = distance + step_dist
            if neighbour == target:
                paths_to_end.append((new_path, new_dist))
            else:
                queue.append((new_dist, neighbour, new_path))

    paths_to_end.sort(key=lambda x: x[1], reverse=True)
    #print(paths_to_end)
    longest = paths_to_end[0][1]
    
    return longest
    

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        test_lines = f.readlines()

    with open('input.txt', 'r') as f:
        input_lines = f.readlines()
    
    #print("Part 1 ======================")
    #test_vals = part_1(test_lines)
    #print(f"Test output: {test_vals}")
    #input_vals = part_1(input_lines)
    #print(f"Real output: {input_vals}")

    print("Part 2 ======================")
    test_vals = part_2(test_lines)
    print(f"Test output: {test_vals}")
    input_vals = part_2(input_lines)
    print(f"Real output: {input_vals}")