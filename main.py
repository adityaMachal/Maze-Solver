from maze import random_maze
from algorithms import bfs, dfs, astar, dijkstra
from gui_turtle import Drawer

def choose_algo(n):
    if n == '1':
        return dfs
    if n == '2':
        return bfs
    if n == '3':
        return astar
    if n == '4':
        return dijkstra
    return bfs

def main():
    print("Maze Solver (beginner style)")
    print("Choose algorithm: (1) DFS  (2) BFS  (3) A*  (4) Dijkstra")
    n = input("Enter number [2]: ").strip()
    if n == '':
        n = '2'
    algo = choose_algo(n)
    dims = input("Enter rows cols (e.g. 21 21) or press Enter for default 21 21: ").strip()
    if dims:
        parts = dims.split()
        try:
            r = int(parts[0])
            c = int(parts[1]) if len(parts) > 1 else r
        except:
            r, c = 21, 21
    else:
        r, c = 21, 21
    maze = random_maze(r, c)
    size = max(6, min(22, 600 // max(r, c)))
    drawer = Drawer(maze, cellsize = size, delay=25)
    gen = algo(maze)
    drawer.visualize(gen)

if __name__ == '__main__':
    main()
