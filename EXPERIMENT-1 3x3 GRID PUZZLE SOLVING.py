def is_goal(puzzle):
    for i in range(8):
        if puzzle[i] != i+1:
            return False
    return puzzle[8] == 0
def print_puzzle(puzzle):
    for i in range(9):
        print(puzzle[i], end=" ")
        if i % 3 == 2:
            print()
def get_blank_position(puzzle):
    return puzzle.index(0)
def slide(puzzle, direction):
    blank = get_blank_position(puzzle)
    swap = blank + direction
    puzzle[blank], puzzle[swap] = puzzle[swap], puzzle[blank]
def solve(puzzle):
    while not is_goal(puzzle):
        row, col = get_blank_position(puzzle) // 3, get_blank_position(puzzle) % 3
        if row > 0:
            slide(puzzle, -3)
        elif row < 2:
            slide(puzzle, 3)
        if col > 0:
            slide(puzzle, -1)
        elif col < 2:
            slide(puzzle, 1)
        print_puzzle(puzzle)
puzzle = [2, 4, 1, 8, 3, 7, 6, 5, 0]
print("Initial State:")
print_puzzle(puzzle)
print()
solve(puzzle)
