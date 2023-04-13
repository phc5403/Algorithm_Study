# PASS하고 이상해서 구글링하다가
# 나처럼 슬라이싱 복잡하게 안하고
# 그냥 단순하게 [idx:idx] 끼워넣기했길래 내코드에 적용해서 시험 제출하는것

def solution(lst):
    global origin, mid

    check = lst[0]
    # 규칙이 원본에서 "앞에서부터 뒤로 검색"을 해야함
    mid += N

    for i in range(mid):
        if origin[i] > check:
            #origin = origin[:i] + lst + origin[i:]
            origin[i:i] = lst
            return

    for j in range(mid, len(origin)):
        if origin[j] > check:
            #origin = origin[:j] + lst + origin[j:]
            origin[i:i] = lst
            return

    origin.extend(lst)


TC = int(input())

for tc in range(1, TC + 1):
    # 각 수열의 길이, 수열의 개수
    # 5 <= N <= 1000, 1 <= M <= 1000, 6 <= L <= N+M
    N, M = map(int, input().split())

    origin = list(map(int, input().split()))
    branch = [list(map(int, input().split())) for _ in range(M-1)]

    # 기본적으로 수열N개, 규칙 2개 / 수열이 N+1개 이상이면 규칙들을 반복 적용
    mid = 0
    for k in range(M-1):
        solution(branch[k])

    print(f'#{tc} ', end='')
    print(*origin[-1: len(origin)-11: -1])
