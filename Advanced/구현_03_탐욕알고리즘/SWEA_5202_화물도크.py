## 활동 선택 문제 ##
from collections import deque


def locally_optimal_choice(qu):
    global cnt

    start, end = qu.popleft()
    cnt += 1
    temp = deque()

    while qu:
        s, e = qu.popleft()

        if end <= s:
            temp.append([s, e])

    if temp:
        locally_optimal_choice(temp)

    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    activity = deque(sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1]))

    cnt = 0
    locally_optimal_choice(activity)

    print(f'#{tc} {cnt}')
