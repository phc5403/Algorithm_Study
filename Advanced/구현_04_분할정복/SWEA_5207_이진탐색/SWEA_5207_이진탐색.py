def binary_search(key):
    global A

    start, end = 0, N - 1

    # Default= -1, Left= 1, Right= 0
    switch = -1

    while start <= end:
        mid = (start + end) // 2

        if key == A[mid]:
            return 1

        # Left area
        elif key < A[mid]:
            if switch == 1:  # 같은 방향이면 return
                return 0
            else:  # 방향 갱신
                switch = 1

            end = mid - 1

        # Right area
        else:  # key > A[mid]
            if switch == 0:  # 같은 방향이면 return
                return 0
            else:  # 방향 갱신
                switch = 0

            start = mid + 1

    return 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(sorted(map(int, input().split())))
    cnt = 0

    for k in map(int, input().split()):
        cnt += binary_search(k)

    print(f'#{tc} {cnt}')

