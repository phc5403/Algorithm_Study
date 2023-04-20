from collections import deque
import time


def bfs():
    global res

    cnt = 0  # while-qu.popleft() 횟수
    what = 0  # 누적합 >= res 가지치기 횟수

    qu = deque()
    qu.append([0, 0, lst[0][0]])

    while qu:
        cnt += 1

        x, y, cumulative_sum = qu.popleft()

        if cumulative_sum >= res:
            what += 1
            continue

        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx <= N-1 and 0 <= ny <= N-1:
                if nx == N-1 and ny == N-1:
                    res = min(res, cumulative_sum + lst[nx][ny])

                else:
                    qu.append([nx, ny, cumulative_sum + lst[nx][ny]])

    # print(f'CNT, WHAT = {cnt}, {what}')
    return


for tc in range(1, int(input()) + 1):
    # 3 <= N <= 13
    N = int(input())

    lst = [list(map(int, input().split()))for _ in range(N)]

    dx = [1, 0]
    dy = [0, 1]
    res = float('inf')

    start = time.time()
    bfs()

    print(f'#{tc} {res}')

    end = time.time()
    # print(f'{round(int(end-start) * 1000)}ms')
    
