# Review - AoC 2023

## What I've learned

- `graphviz`
  - one problem required analysing the structure of the input in order to solve
  - graphviz was helpful for this, but I also used it on other days when debugging my solutions
- shoelace formula and pick's theorem: calculating area of a polygon given vertices
- Python specific tools
  - `functools` - `@cache` for dynamic programming
  - `heapq` - priority queue
  - `deepcopy` - useful for copying nested data structures
- keep it simple stupid: start with brute force. If the time complexity is good enough, don't bother with anything else until you see it's necessary. An exception would be if you know a more efficient algorithm that is also simpler to implement than brute force - e.g. you know a mathematical formula to directly compute the result
- having a skeleton template to read in the test/input and run parts 1 and 2 is very handy
  - improvements: set up for multiple test cases, and include assertions for expected results
- would be good to unify some helper functions in a utils file
  - e.g. grid printing
  - have templates for Dijkstra's, bfs, dfs ready to go
- diagrams are often very helpful
- often you can skip a lot of the detail in the description. That said - before spending time debugging, ensure you read the spec correctly. Sometimes the wording is confusing, and the test output will not make this clear
