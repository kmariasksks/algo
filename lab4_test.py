import queue
import unittest

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

class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        matrix = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]
        start = (0, 0)
        end = (7, 5)
        self.assertEqual(shortest_path(matrix, start, end), 12)

if __name__ == '__main__':
    unittest.main()
