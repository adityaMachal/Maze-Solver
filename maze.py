import random

class Maze:
    def __init__(self, rows, cols, grid=None):
        self.rows = rows
        self.cols = cols
        if grid:
            self.grid = grid
        else:
            self.grid = [[1 for _ in range(cols)] for _ in range(rows)]
        self.start = (1, 1)
        self.end = (rows - 2, cols - 2)

def random_maze(rows, cols):
    if rows % 2 == 0:
        rows += 1
    if cols % 2 == 0:
        cols += 1
    grid = [[1 for _ in range(cols)] for _ in range(rows)]
    def carve(r, c):
        grid[r][c] = 0
        dirs = [(0,2),(0,-2),(2,0),(-2,0)]
        random.shuffle(dirs)
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 1 <= nr < rows-1 and 1 <= nc < cols-1 and grid[nr][nc] == 1:
                grid[r + dr//2][c + dc//2] = 0
                carve(nr, nc)
    carve(1, 1)
    m = Maze(rows, cols, grid)
    m.start = (1, 1)
    m.end = (rows-2, cols-2)
    if m.grid[m.end[0]][m.end[1]] == 1:
        m.grid[m.end[0]][m.end[1]] = 0
    return m
