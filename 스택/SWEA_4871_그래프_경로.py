def dfs(cur):
    global end, flag

    if cur == end:
        flag = 1
        return

    for nxt in path[cur]:
        dfs(nxt)
    return


TC = int(input())

for tc in range(1, TC + 1):
    V, E = map(int, input().split())

    edge = [list(map(int, input().split())) for _ in range(E)]
    path = [[] for _ in range(V + 1)]
    start, end = map(int, input().split())
    flag = 0

    for a, b in edge:
        path[a].append(b)
        # path[b].append(a)

    dfs(start)
    print(f'#{tc} {flag}')
