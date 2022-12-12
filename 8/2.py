input = open("8/input.txt", "r")
grid = [list(line[:-1]) for line in input.readlines()]
score = 0


def get_index(trees, value):
    for i, elem in enumerate(trees):
        if elem >= value:
            return i
    return -1


for row in range(1, len(grid)-1):
    for col in range(1, len(grid[row])-1):
        value = grid[row][col]
        grid_row = grid[row]
        grid_col = [r[col] for r in grid]
        left = col if get_index(
            grid_row[:col], value) == -1 else get_index(reversed(grid_row[:col]), value)+1
        right = len(grid_row)-1-col if get_index(
            grid_row[col+1:], value) == -1 else get_index(grid_row[col+1:], value)+1
        top = row if get_index(
            grid_col[:row], value) == -1 else get_index(reversed(grid_col[:row]), value)+1
        down = len(grid_row)-1-row if get_index(
            grid_col[row+1:], value) == -1 else get_index(grid_col[row+1:], value)+1
        score = max(score, left*right*top*down)

print(score)
