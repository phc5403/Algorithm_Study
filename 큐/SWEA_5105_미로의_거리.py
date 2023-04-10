from collections import deque


def bfs(x, y):
    qu = deque()
    qu.append([x, y, 0])
    visited = [[False] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while qu:
        x, y, cnt = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and not visited[nx][ny]:
                if maze[nx][ny] == 3:
                    print(f'#{tc} {cnt}')
                    return

                if not maze[nx][ny]:
                    visited[nx][ny] = True
                    qu.append([nx, ny, cnt + 1])

    return print(f'#{tc} 0')


TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                bfs(r, c)
                break
