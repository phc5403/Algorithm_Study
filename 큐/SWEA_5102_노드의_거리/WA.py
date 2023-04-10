def dfs(cur, cnt):
    global G, flag

    visited[cur] = True

    if cur == G:
        print(f'#{tc} {cnt}')
        flag = 1
        return

    for nxt in path[cur]:
        if not visited[nxt]:
            dfs(nxt, cnt + 1)


TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    path = [[] for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]

    for a, b in edge:
        path[a].append(b)
        path[b].append(a)

    flag = 0
    if S == G:
        print(f'#{tc} 1')
        flag = 1
    else:
        dfs(S, 0)

    if not flag:
        print(f'#{tc} 0')
