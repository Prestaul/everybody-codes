from utils import test
import copy

def solve(input):
    grid = [[int(c) for c in line] for line in input.replace('.', '0').replace('#', '1').splitlines()]

    depth = 1;
    changed = True
    while (changed):
        changed = False
        next = copy.deepcopy(grid)
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] != depth:
                    continue;
                if (grid[y-1][x] == depth and grid[y+1][x] == depth and grid[y][x-1] == depth and grid[y][x+1] == depth):
                    next[y][x] = depth + 1
                    changed = True

        depth += 1
        grid = next

    return sum([c for row in grid for c in row])

def solve3(input):
    grid = [[int(c) for c in line] for line in input.replace('.', '0').replace('#', '1').splitlines()]
    w = len(grid[0])
    h = len(grid)

    get = lambda x, y: grid[y][x] if 0 <= x < w and 0 <= y < h else 0

    depth = 1;
    changed = True
    while (changed):
        changed = False
        next = copy.deepcopy(grid)
        for x in range(w):
            for y in range(h):
                if grid[y][x] != depth:
                    continue;
                if (grid[y][x] == depth and get(x-1,y-1) == depth and get(x,y-1) == depth and get(x+1,y-1) == depth and get(x-1,y) == depth and get(x,y) == depth and get(x+1,y) == depth and get(x-1,y+1) == depth and get(x,y+1) == depth and get(x+1,y+1) == depth):
                    next[y][x] = depth + 1
                    changed = True

        depth += 1
        grid = next

    # print('\n'.join([''.join([str(c) for c in row]) for row in grid]))

    return sum([c for row in grid for c in row])

example = '''
..........
..###.##..
...####...
..######..
..######..
...####...
..........'''.strip()

test(solve, example, expected=35)
test(solve, file='03-1', expected=114)
test(solve, file='03-2', expected=2673)
test(solve3, example, expected=29)
test(solve3, file='03-3', expected=10423)
