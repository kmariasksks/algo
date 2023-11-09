import queue

class Graph:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def neighbors(self, x, y):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if self.is_valid(new_x, new_y) and self.matrix[new_x][new_y] == 1:
                yield (new_x, new_y)

def shortest_path(graph, start, end):
    visited = [[False for _ in range(graph.cols)] for _ in range(graph.rows)]

    q = queue.Queue()
    q.put((start[0], start[1], 0))

    while not q.empty():
        x, y, dist = q.get()
        if (x, y) == end:
            return dist

        for neighbor_x, neighbor_y in graph.neighbors(x, y):
            if not visited[neighbor_x][neighbor_y]:
                q.put((neighbor_x, neighbor_y, dist + 1))
                visited[neighbor_x][neighbor_y] = True

    return -1

with open('input.txt', 'r') as file:
    start_x, start_y = map(int, file.readline().strip().split(', '))
    end_x, end_y = map(int, file.readline().strip().split(', '))
    rows, cols = map(int, file.readline().strip().split(','))
    matrix = [list(map(int, file.readline().strip().split())) for _ in range(rows)]

graph = Graph(rows, cols, matrix)
result = shortest_path(graph, (start_x, start_y), (end_x, end_y))

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Найкоротший шлях від ({start_x}, {start_y}) до ({end_x}, {end_y}): {result}")