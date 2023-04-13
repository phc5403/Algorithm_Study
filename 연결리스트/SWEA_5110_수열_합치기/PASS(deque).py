from collections import deque


def solution(lst):
    global origin, mid

    check = lst[0]
    # 규칙이 원본에서 "앞에서 -> 뒤로 검색"을 해야함
    mid += N

    # TLE를 피하기 위해 수열을 절반씩만 검사함
    for i in range(mid):
        if origin[i] > check:
            while lst:
                origin.insert(i, lst.pop())
            return
    
    # 앞절반에서 원하는값을 못 찾을 경우, 뒷절반 검사
    for j in range(mid, len(origin)):
        if origin[j] > check:
            while lst:
                origin.insert(j, lst.pop())
            return

    # 수열 N + 1의 첫 숫자보다 큰 숫자가 없으면, 맨 뒤에 붙임
    origin.extend(lst)


TC = int(input())

for tc in range(1, TC + 1):
    # 각 수열의 길이, 수열의 개수
    # 5 <= N <= 1000, 1 <= M <= 1000, 6 <= L <= N+M
    N, M = map(int, input().split())

    # 계속 규칙이 적용될 원본, 그 뒤의 수열
    origin = deque(map(int, input().split()))
    branch = deque()

    for _ in range(M-1):
        branch.append(deque(map(int, input().split())))

    # 기본적으로 수열N개, 규칙 2개 / 수열이 N+1개 이상이면 규칙들을 반복 적용
    mid = 0
    while branch:
        solution(branch.popleft())

    print(f'#{tc} ', end='')

    for res in range(mid + N-1, mid+N-11, -1):
        print(origin[res], end=' ')

    print()
