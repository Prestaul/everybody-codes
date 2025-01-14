import os, sys

def read(file):
    path = os.path.join(os.path.dirname(sys.argv[0]), f'./inputs/{file}.txt')
    with open(path, 'r') as input:
        return input.read()

def test(solve, /, input = None, *, file = None, expected = None, strip_input = True, args = {}):
    if input == None:
        input = read(file)
    if strip_input:
        input = input.strip();
    result = solve(input, **args)
    if expected == None:
        print(f'{solve.__name__:>30} -> {result}')
    elif result != expected:
        print(f'\033[91m{solve.__name__:>30} -> {result} (expected {expected})\033[0m')
    else:
        print(f'\033[92m{solve.__name__:>30} -> {result}\033[0m')
