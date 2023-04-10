from collections import deque

TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())

    qu = deque()

    for s in list(map(int, input().split())):
        qu.append(s)

    for _ in range(K):
        qu.rotate(-1)

    print(f'#{tc} {qu.popleft()}')

