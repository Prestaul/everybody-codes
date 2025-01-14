from utils import test
import re

def solve(input):
    nums = [int(n) for n in input.splitlines()]
    m = min(nums)
    return sum([n - m for n in nums])

def solve3(input):
    nums = [int(n) for n in input.splitlines()]
    m = min(nums)
    strikes = 2**63 - 1
    next = sum([abs(n - m) for n in nums]);
    while (next < strikes):
        strikes = next
        m += 1000
        next = sum([abs(n - m) for n in nums])

    strikes = next
    m -= 1
    next = sum([abs(n - m) for n in nums])
    while (next < strikes):
        strikes = next
        m -= 1
        next = sum([abs(n - m) for n in nums])

    return strikes

example = '''
3
4
7
8'''

test(solve, example, expected=10)
test(solve, file='04-1', expected=88)
test(solve, file='04-2', expected=959045)
test(solve3, '''
2
4
5
6
8''', expected=8)
test(solve3, file='04-3', expected=121611606)

print('\n----------------------------- DONE -----------------------------\n')
