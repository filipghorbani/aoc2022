input = open("8/input.txt", "r")
grid = [list(line[:-1]) for line in input.readlines()]
visible = (2*len(grid) + 2*len(grid[0]))-4

for row in range(1, len(grid)-1):
    for col in range(1, len(grid[row])-1):
        value = grid[row][col]
        grid_row = grid[row]
        grid_col = [r[col] for r in grid]
        if (max(grid_row[:col]) < value or max(grid_row[col+1:]) < value or max(grid_col[:row]) < value or max(grid_col[row+1:]) < value):
            visible += 1
print(visible)
