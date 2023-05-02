from collections import deque


def bfs(student):
    global cnt

    qu = deque()
    qu.append(student)

    visited[student] = True

    while qu:
        cur = qu.popleft()

        for nxt in edge[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                qu.append(nxt)

    return


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    edge = [[] for _ in range(N + 1)]

    for idx in range(0, len(lst), 2):
        edge[lst[idx]].append(lst[idx + 1])
        edge[lst[idx + 1]].append(lst[idx])

    # 2 <= N <= 100, 1 <= M <= 100
    # 최소 2명, 최소 1쌍 => 팀은 1개 이상임

    cnt = 0
    visited = [False] * (N+1)
    for stu in range(1, N+1):
        if not visited[stu]:
            bfs(stu)
            cnt += 1

    print(f'#{tc} {cnt}')
