from utils import test

def dump(grid):
    cols = [[r[i] if i < len(r) else " " for r in grid] for i in range(max([len(row) for row in grid]))]
    print('\n'.join([' '.join([str(c) for c in col]) for col in cols]))

def solve(input, limit):
    grid = ([[int(n) for n in l.split()] for l in input.splitlines()])
    cols = [[r[i] for r in grid] for i in range(len(grid[0]))]
    # dump(cols)

    c = 0
    while(limit > 0):
        limit -= 1
        claps = cols[c].pop(0)
        # print('limit', limit, 'claps', claps)
        c = (c + 1) % len(cols)
        idx = claps-1 % (len(cols[c]) * 2)
        if idx > len(cols[c]):
            idx = len(cols[c]) * 2 - idx
        cols[c].insert(idx, claps)
        # print(int(''.join([str(col[0]) for col in cols])))
        # dump(cols)


    return int(''.join([str(col[0]) for col in cols]))

def solve2(input):
    grid = ([[int(n) for n in l.split()] for l in input.splitlines()])
    cols = [[r[i] for r in grid] for i in range(len(grid[0]))]
    # dump(cols)

    c = 0
    i = 0
    visited = {}
    while(True):
        i += 1
        claps = cols[c].pop(0)
        # print('limit', limit, 'claps', claps)
        c = (c + 1) % len(cols)
        idx = claps-1 % (len(cols[c]) * 2)
        if idx > len(cols[c]):
            idx = len(cols[c]) * 2 - idx
        cols[c].insert(idx, claps)

        val = ''.join([str(col[0]) for col in cols])
        # print(val)
        if val in visited:
            prev = visited.get(val)
            inc = i - prev
            print(prev, i, inc, int(val), 2024 * inc - (inc - prev) )
            return int(val) * (2024 * inc - (inc - prev))
        visited[val] = i

        # dump(cols)


    return int(''.join([str(col[0]) for col in cols]))

example = '''
2 3 4 5
3 4 5 2
4 5 2 3
5 2 3 4'''

test(solve, example, args={ 'limit': 1 }, expected=3345)
test(solve, example, args={ 'limit': 10 }, expected=2323)
test(solve, file='05-1', args={ 'limit': 10 }, expected=2422)
test(solve2, '2 3 4 5\n6 7 8 9', expected=50877075)
test(solve2, file='05-2', expected=None)
# ALL WRONG 55644892657
# test(solve, file='05-3', expected=None)

print('\n----------------------------- DONE -----------------------------\n')
