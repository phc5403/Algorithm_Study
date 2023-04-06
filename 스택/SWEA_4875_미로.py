from collections import deque
from pprint import pprint

def bfs(sx, sy):
    qu = deque()
    qu.append([sx, sy])
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True

    while qu:
        x, y = qu.pop()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and not visited[nx][ny]:
                if maze[nx][ny] == 3:
                    print(f'#{tc} 1')
                    return

                if not maze[nx][ny]:
                    visited[nx][ny] = True
                    qu.append([nx, ny])

    print(f'#{tc} 0')
    return


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())

    maze = [list(map(int, input().strip())) for _ in range(N)]
    sx, sy = 0, 0

    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                sx, sy = row, col
                break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    bfs(sx, sy)
