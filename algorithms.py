from collections import deque
import heapq

def bfs(maze):
    start = maze.start
    goal = maze.end
    q = deque([start])
    visited = set([start])
    parent = {}
    yield {'current': None, 'frontier': set(q), 'visited': set(visited), 'solution': None}
    while q:
        cur = q.popleft()
        yield {'current': cur, 'frontier': set(q), 'visited': set(visited), 'solution': None}
        if cur == goal:
            path = []
            node = cur
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            yield {'current': cur, 'frontier': set(q), 'visited': set(visited), 'solution': path}
            return
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = cur[0] + dr
            nc = cur[1] + dc
            nb = (nr, nc)
            if 0 <= nr < maze.rows and 0 <= nc < maze.cols and maze.grid[nr][nc] == 0 and nb not in visited:
                visited.add(nb)
                parent[nb] = cur
                q.append(nb)
                yield {'current': cur, 'frontier': set(q), 'visited': set(visited), 'solution': None}

def dfs(maze):
    start = maze.start
    goal = maze.end
    stack = [start]
    visited = set([start])
    parent = {}
    yield {'current': None, 'frontier': set(stack), 'visited': set(visited), 'solution': None}
    while stack:
        cur = stack.pop()
        yield {'current': cur, 'frontier': set(stack), 'visited': set(visited), 'solution': None}
        if cur == goal:
            path = []
            node = cur
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            yield {'current': cur, 'frontier': set(stack), 'visited': set(visited), 'solution': path}
            return
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = cur[0] + dr
            nc = cur[1] + dc
            nb = (nr, nc)
            if 0 <= nr < maze.rows and 0 <= nc < maze.cols and maze.grid[nr][nc] == 0 and nb not in visited:
                visited.add(nb)
                parent[nb] = cur
                stack.append(nb)
                yield {'current': cur, 'frontier': set(stack), 'visited': set(visited), 'solution': None}

def astar(maze):
    start = maze.start
    goal = maze.end
    def h(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_heap = []
    heapq.heappush(open_heap, (h(start,goal), 0, start))
    gscore = {start: 0}
    parent = {}
    open_set = {start}
    closed = set()
    yield {'current': None, 'frontier': set(open_set), 'visited': set(closed), 'solution': None}
    while open_heap:
        _, _, cur = heapq.heappop(open_heap)
        if cur in closed:
            continue
        open_set.discard(cur)
        closed.add(cur)
        yield {'current': cur, 'frontier': set(open_set), 'visited': set(closed), 'solution': None}
        if cur == goal:
            path = []
            node = cur
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            yield {'current': cur, 'frontier': set(open_set), 'visited': set(closed), 'solution': path}
            return
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = cur[0] + dr
            nc = cur[1] + dc
            nb = (nr, nc)
            if 0 <= nr < maze.rows and 0 <= nc < maze.cols and maze.grid[nr][nc] == 0 and nb not in closed:
                tentative = gscore[cur] + 1
                if tentative < gscore.get(nb, 1e9):
                    gscore[nb] = tentative
                    parent[nb] = cur
                    f = tentative + h(nb, goal)
                    heapq.heappush(open_heap, (f, tentative, nb))
                    open_set.add(nb)
                    yield {'current': cur, 'frontier': set(open_set), 'visited': set(closed), 'solution': None}

def dijkstra(maze):
    start = maze.start
    goal = maze.end
    heap = []
    heapq.heappush(heap, (0, start))
    dist = {start: 0}
    parent = {}
    visited = set()
    frontier = {start}
    yield {'current': None, 'frontier': set(frontier), 'visited': set(visited), 'solution': None}
    while heap:
        d, cur = heapq.heappop(heap)
        if cur in visited:
            continue
        frontier.discard(cur)
        visited.add(cur)
        yield {'current': cur, 'frontier': set(frontier), 'visited': set(visited), 'solution': None}
        if cur == goal:
            path = []
            node = cur
            while node != start:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            yield {'current': cur, 'frontier': set(frontier), 'visited': set(visited), 'solution': path}
            return
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = cur[0] + dr
            nc = cur[1] + dc
            nb = (nr, nc)
            if 0 <= nr < maze.rows and 0 <= nc < maze.cols and maze.grid[nr][nc] == 0 and nb not in visited:
                nd = d + 1
                if nd < dist.get(nb, 1e9):
                    dist[nb] = nd
                    parent[nb] = cur
                    heapq.heappush(heap, (nd, nb))
                    frontier.add(nb)
                    yield {'current': cur, 'frontier': set(frontier), 'visited': set(visited), 'solution': None}
