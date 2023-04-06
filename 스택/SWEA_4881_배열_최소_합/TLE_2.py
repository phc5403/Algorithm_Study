import time


def n_queens(row, queen, cumulative_sum):
    global res

    # END : 모든 행을 검사했다면, 최소 결괏값 갱신
    if row == N:
        res = min(res, cumulative_sum)
        return

    # 재귀 + 비트마스킹으로 놓을 수 있는 위치 판단
    # ==> 부분 집합 알고리즘과 비슷한것같음.
    for col in range(N):
        # 방문 안한 곳이면:
        if not queen[col]:
            queen[col] = 1  # 방문 표시(=1)
            # 방문할 수 있으니 그곳에 해당하는 List의 값을 누적하여 재귀 호출()
            n_queens(row + 1, queen, cumulative_sum + lst[row][col])
            queen[col] = 0  # 다음 위치를 위해 방문 표시 제거


TC = int(input())

for tc in range(1, TC+1):
    # 3 <= N <= 10
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    res = float('inf')

    start = time.time()  ##
    
    q = [0] * N  # 방문 위치 배열을 개수에 맞게 0으로 주고 시작.

    # (시작 행, 방문 배열, 시작 누적합)
    n_queens(0, q, 0)
    print(f'#{tc} {res}')

    end = time.time()  ##
    # print(f'{round(int((end - start) * 1000))} ms')
