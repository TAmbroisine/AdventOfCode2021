import os
from turtle import width

DAY = 4


def get_input():
    """Get the input from a txt file"""
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/InputDay{}.txt".format(path, DAY)) as Input:
        Input_r = Input.read()
        numbers, grids, score_cards = parse(Input_r)
    return numbers, grids, score_cards


def parse(input_s):
    """Organize data"""
    numbers, *grids = input_s.split('\n\n')
    numbers = [int(n) for n in numbers.split(',')]
    score_cards = [create_score_grid(grid) for grid in grids]
    grids = [parse_grid(grid) for grid in grids]
    return numbers, grids, score_cards


def parse_grid(grid_s: str) -> dict:
    """create the grids with the parsed data"""
    lines = [[int(n) for n in line.split()] for line in grid_s.splitlines()]
    grid = {}
    for i, line in enumerate(lines):
        for j, n in enumerate(line):
            grid[n] = (i, j)
    return grid


def create_score_grid(grid_s):
    """create score grids with the same dimensions as the normal grids"""
    lines = [[int(n) for n in line.split()] for line in grid_s.splitlines()]
    height = len(lines)
    width = len(lines[0])
    return [[False] * width for _ in range(height)]


def mark(n, grid, score_card):
    """Flag spot on the score card"""
    if n in grid:
        i, j = grid[n]
        score_card[i][j] = True


def transpose(score_card):
    """Return a transpose of the original score card
    Ex: [[1, 2], [3, 4]] -> [[1, 3], [2, 4]]
    Hint: use the zip() builtin
    """
    return list(zip(*score_card))


def check_rows(score_card):
    """Check if a row is all True

    Hint: use any() and all() builtins
    """
    return any(all(row) for row in score_card)


def has_bingo(score_card):
    """Check if a score card has a bingo"""
    return check_rows(score_card) or\
        check_rows(transpose(score_card))


def part1(numbers, grids, score_cards):
    """Resolve the first part of the problem"""
    for n in numbers:
        for grid, score_card in zip(grids, score_cards):
            mark(n, grid, score_card)
            if has_bingo(score_card, grid):
                return grid['unmarked_sum'] * n


def part_2(numbers, grids, score_cards):
    """Resolve the second part of the problem"""
    grid, sc, n = last_bingo(numbers, grids, score_cards)
    return sum_unmarked(grid, sc) * n


def last_bingo(numbers, grids, score_cards):
    """Find the last card that had a bingo"""
    bingo = []
    no_bingo = zip(grids, score_cards)
    while numbers or no_bingo:
        still_no_bingo = []
        # n = numbers.pop()
        n, *numbers = numbers
        for (g, sc) in no_bingo:
            mark(n, g, sc)
            if has_bingo(sc):
                bingo.append((g, sc, n))
            else:
                still_no_bingo.append((g, sc))
        no_bingo = still_no_bingo
    return bingo[-1]


def sum_unmarked(grid, score_card):
    """do the sum of every unmarked numbers on a grid"""
    s = 0
    for (n, (i, j)) in grid.items():
        if not score_card[i][j]:
            s += n
    return s


if __name__ == "__main__":
    numbers, grids, score_cards = get_input()
    # print(part1(numbers,grids,score_cards))
    print(part_2(numbers, grids, score_cards))
