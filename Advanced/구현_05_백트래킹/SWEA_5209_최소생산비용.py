def backtracking(row, cumulative_sum, bit):
    global res

    # Pruning
    if cumulative_sum >= res:
        return

    # END condition
    if row == N:
        res = min(res, cumulative_sum)
        return

    for k in range(N):
        if not bit[k]:
            bit[k] = 1
            backtracking(row + 1, cumulative_sum + lst[row][k], bit)
            bit[k] = 0

    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(N)]

    bit_array = [0] * N
    res = float('inf')

    backtracking(0, 0, bit_array)
    print(f'#{tc} {res}')
