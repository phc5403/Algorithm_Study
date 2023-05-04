from collections import deque


def bfs():
    qu = deque([[0, 0]])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 거리(가중치)
    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = 0

    while qu:
        x, y = qu.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                # 높이 차 계산
                if lst[x][y] < lst[nx][ny]:
                    nxt = distance[x][y] + 1 + (lst[nx][ny] - lst[x][y])
                else:
                    nxt = distance[x][y] + 1

                # 더 적은 연비일 경우 거리 List값 갱신
                if nxt < distance[nx][ny]:
                    distance[nx][ny] = nxt
                    qu.append([nx, ny])

    return distance[N-1][N-1]


for tc in range(1, int(input()) + 1):
    # 3 <= N <= 100, 0 <= H < 1000
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {bfs()}')
