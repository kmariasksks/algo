import queue

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = queue.Queue()
    q.put((start[0], start[1], 0))

    while not q.empty():
        x, y, dist = q.get()
        if (x, y) == end:
            return dist

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and matrix[new_x][new_y] == 1:
                q.put((new_x, new_y, dist + 1))
                visited[new_x][new_y] = True

    return -1

with open('input.txt', 'r') as file:
    start_x, start_y = map(int, file.readline().strip().split(', '))
    end_x, end_y = map(int, file.readline().strip().split(', '))
    rows, cols = map(int, file.readline().strip().split(','))
    matrix = [list(map(int, file.readline().strip().split())) for _ in range(rows)]

result = shortest_path(matrix, (start_x, start_y), (end_x, end_y))

with open('output.txt', 'w') as file:
    file.write(str(result))

print(f"Найкоротший шлях від ({start_x}, {start_y}) до ({end_x}, {end_y}): {result}")
