import time


def dfs(x, y, cumulative_sum):
    global res, cnt, what

    cumulative_sum += lst[x][y]

    cnt += 1  ##

    if res <= cumulative_sum:
        what += 1  ##
        return

    if x == N-1 and y == N-1:
        res = min(res, cumulative_sum)
        return

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            dfs(nx, ny, cumulative_sum)



for tc in range(1, int(input()) + 1):
    # 3 <= N <= 13
    N = int(input())

    lst = [list(map(int, input().split()))for _ in range(N)]

    dx = [1, 0]
    dy = [0, 1]
    res = float('inf')

    cnt = 0  # while-qu.popleft() 횟수
    what = 0  # 누적합 >= res 가지치기 횟수

    start = time.time()
    dfs(0, 0, 0)

    print(f'#{tc} {res}')
    # print(f'CNT, WHAT = {cnt}, {what}')

    end = time.time()
    # print(f'{round(int(end-start) * 1000)}ms')
