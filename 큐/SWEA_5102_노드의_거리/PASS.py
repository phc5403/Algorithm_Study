from collections import deque


def bfs(s):
    global G
    qu = deque()
    qu.append([s, 0])

    visited = [False for _ in range(V + 1)]
    visited[s] = True

    while qu:
        cur, cnt = qu.popleft()

        if cur == G:
            print(f"#{tc} {cnt}")
            return

        for nxt in path[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                qu.append([nxt, cnt + 1])

    print(f'#{tc} 0')


TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())
    path = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = list(map(int, input().split()))
        path[a].append(b)
        path[b].append(a)

    S, G = map(int, input().split())

    bfs(S)
