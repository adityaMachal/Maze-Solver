import turtle
import time

CELL_COLORS = {
    'wall': 'black',
    'empty': 'white',
    'visited': '#9dd3f0',
    'frontier': '#bff0b8',
    'current': '#f2d04b',
    'start': '#00cc00',
    'end': '#ff2222',
    'solution': '#f7c7f7'
}

class Drawer:
    def __init__(self, maze, cellsize=20, delay=25):
        self.maze = maze
        self.cellsize = cellsize
        self.delay = delay
        self.rows = maze.rows
        self.cols = maze.cols
        self.screen = turtle.Screen()
        w = self.cols * self.cellsize
        h = self.rows * self.cellsize
        self.screen.setup(width=w+40, height=h+40)
        self.screen.title("Maze Solver - Visualizer")
        turtle.tracer(0, 0)
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.origin_x = -w/2
        self.origin_y = h/2
        self.prev_current = None
        self.draw_base()

    def cell_to_xy(self, r, c):
        x = self.origin_x + c * self.cellsize
        y = self.origin_y - r * self.cellsize
        return x, y

    def draw_square(self, r, c, color):
        x, y = self.cell_to_xy(r, c)
        s = self.cellsize
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(s)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()

    def draw_base(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze.grid[r][c] == 1:
                    self.draw_square(r, c, CELL_COLORS['wall'])
                else:
                    self.draw_square(r, c, CELL_COLORS['empty'])
        s = self.maze.start
        e = self.maze.end
        self.draw_square(s[0], s[1], CELL_COLORS['start'])
        self.draw_square(e[0], e[1], CELL_COLORS['end'])
        turtle.update()

    def visualize(self, generator):
        self.gen = generator
        self.last_solution = None
        self.screen.ontimer(self.step, self.delay)
        self.screen.mainloop()

    def step(self):
        try:
            state = next(self.gen)
        except StopIteration:
            return
        visited = state.get('visited') or set()
        frontier = state.get('frontier') or set()
        cur = state.get('current')
        sol = state.get('solution')

        if sol is None:
            sol_set = set()
        else:
            try:
                sol_set = set(sol)
            except TypeError:
                sol_set = set()

        if self.prev_current and self.prev_current not in sol_set:
            if self.prev_current in visited:
                self.draw_square(self.prev_current[0], self.prev_current[1], CELL_COLORS['visited'])
            else:
                self.draw_square(self.prev_current[0], self.prev_current[1], CELL_COLORS['empty'])
            self.prev_current = None

        for pos in visited:
            if pos == self.maze.start or pos == self.maze.end:
                continue
            self.draw_square(pos[0], pos[1], CELL_COLORS['visited'])
        for pos in frontier:
            if pos == self.maze.start or pos == self.maze.end:
                continue
            self.draw_square(pos[0], pos[1], CELL_COLORS['frontier'])
        if cur:
            if cur != self.maze.start and cur != self.maze.end:
                self.draw_square(cur[0], cur[1], CELL_COLORS['current'])
            self.prev_current = cur
        if sol:
            for pos in sol:
                if pos == self.maze.start or pos == self.maze.end:
                    continue
                self.draw_square(pos[0], pos[1], CELL_COLORS['solution'])
        turtle.update()
        self.screen.ontimer(self.step, self.delay)
