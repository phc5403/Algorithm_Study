## 문제 의도와는 다른 List 기반 간단한 풀이 ##

TC = int(input())

for tc in range(1, TC + 1):
    # 5 <= N <= 1000, 1 <= M <= 1000, 6 <= L <= N+M
    N, M, L = map(int, input().split())

    # N개의 10억 이하 자연수로 이뤄진 수열
    lst = list(map(int, input().split()))

    for _ in range(M):
        idx, num = map(int, input().split())

        lst.insert(idx, num)

    print(f'#{tc} {lst[L]}')
    
