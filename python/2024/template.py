from utils import test
import re

def solve(input):
    nums = re.findall(r'-?\d+', input)
    return sum([int(a) * int(b) for a, b in zip(nums[::2], nums[1::2])])

example = '''
What is 6 7s?'''

test(solve, example, expected=42)
# test(solve, file='DD-1', expected=None)
# test(solve, file='DD-2', expected=None)
# test(solve, file='DD-3', expected=None)

print('\n----------------------------- DONE -----------------------------\n')
