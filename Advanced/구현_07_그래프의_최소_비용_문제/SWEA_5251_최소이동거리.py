from collections import deque


def bfs():
    qu = deque()

    while edge[0]:
        qu.append(edge[0].pop())

    res = float('inf')

    while qu:
        cur, w = qu.popleft()

        # Pruning
        if res <= w:
            continue
        
        # END
        if cur == N:
            res = min(res, w)

        for nxt, nw in edge[cur]:
            nw += w
            qu.append([nxt, nw])

    return res


for tc in range(1, int(input()) + 1):
    # 1 <= N, start, end <= 1000, 1 <= weight <= 10, 1 <= E <= 1,000,000
    N, E = map(int, input().split())

    edge = [[] for _ in range(N + 1)]

    for _ in range(E):
        start, end, weight = map(int, input().split())
        edge[start].append([end, weight])

    print(f'#{tc} {bfs()}')
