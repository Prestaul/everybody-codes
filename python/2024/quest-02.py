from itertools import product
import inputs

def solve(input):
    l, text = input.split('\n\n')
    runes = l.split(':')[1].split(',')
    sum = 0
    for rune in runes:
        sum += text.count(rune)
    return sum

def solve2(input):
    l, text = input.split('\n\n')
    runes = l.split(':')[1].split(',')
    runes = set(runes + [r[::-1] for r in runes])
    matched = set()
    for rune in runes:
        idx = text.find(rune)
        v = len(rune)
        while(idx != -1):
            for i in range(idx, idx + v):
                matched.add(i)
            idx = text.find(rune, idx + 1)
    return len(matched)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def solve3(input):
    l, text = input.split('\n\n')
    grid = [[c for c in line] for line in text.splitlines()]
    runes = l.split(':')[1].split(',')
    runes = set(runes + [r[::-1] for r in runes])
    matched = set()
    w = len(grid[0])
    h = len(grid)
    for x, y in product(range(w), range(h)):
        for dx, dy in dirs:
            for rune in runes:
                match = True
                for i in range(len(rune)):
                    y2 = y + dy * i
                    if y2 < 0 or y2 >= h or grid[y + dy * i][(x + dx * i) % w] != rune[i]:
                        match = False
                        break

                if match:
                    for i in range(len(rune)):
                        matched.add((y + dy * i, (x + dx * i) % w))

    return len(matched)

print(solve('''
WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE'''.strip()))
print(solve(inputs.read('02-1')))

print(solve2(inputs.read('02-2-example')))
print(solve2(inputs.read('02-2')))

print(solve3('''
WORDS:THE,OWE,MES,ROD,RODEO

HELWORLT
ENIGWDXL
TRODEOAL'''.strip()))

print(solve3(inputs.read('02-3')))
