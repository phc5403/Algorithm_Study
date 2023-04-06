def pruning(qu, c):
    # qu[]가 비어있다 == 처음은 무조건 방문 가능
    if not qu: 
        return True

    for idx in range(len(qu)):
        # 이미 방문한 위치라면 False 반환
        if qu[idx] == c:
            return False

    return True


def n_queens(row, queen):
    global res
    # < END > row + 1해서 넘어온 값이 N이면 == 모두 놓았음.
    if row == N:
        cumulative_sum = 0
        # 방문 위치 기록이 되어있는 queen[]을 이용해,
        # List에서의 누적합 계산
        for x in range(len(queen)):
            cumulative_sum += lst[x][queen[x]]
        
        # 최솟값 갱신
        res = min(res, cumulative_sum)
        return

    for col in range(N):
        # 현재 방문할 위치(col)의 Promising 판단
        if pruning(queen, col):
            queen.append(col)  # 유망하다면, 방문 배열에 저장
            n_queens(row + 1, queen)  # 다음 행으로 재귀 호출
            queen.pop()  # 새로운 위치 추가를 위해 이전 위치 제거


TC = int(input())

for tc in range(1, TC+1):
    # 3 <= N <= 10
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    res = float('inf')

    q = []  # 방문 위치 저장 -> Index = 행 / q[idx] = 열
    
    n_queens(0, q)  # (시작 행, 방문 배열)
    
    print(f'#{tc} {res}')
    
