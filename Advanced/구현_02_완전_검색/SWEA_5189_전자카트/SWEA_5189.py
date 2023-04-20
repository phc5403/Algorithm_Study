def dfs():
    if len(subset) == N-1:
        find_min(subset)  # 2. Find cumulative_sum
        return

    for num in range(2, N+1):
        if num not in subset:
            subset.append(num)
            dfs()
            subset.pop()


def find_min(args):
    global res

    cumulative_sum = 0
    cumulative_sum += lst[0][args[0] - 1]
    cumulative_sum += lst[args[-1] - 1][0]

    for x, y in zip(args, args[1:]):
        cumulative_sum += lst[x-1][y-1]

    res = min(res, cumulative_sum)
    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    res = float('inf')
    subset = []

    dfs()  # 1. Subset
    print(f'#{tc} {res}')

