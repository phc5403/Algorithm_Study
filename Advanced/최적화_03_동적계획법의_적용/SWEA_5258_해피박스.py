from pprint import pprint

### 기본적인 DP: 0-1 knapsack 문제 ###
for tc in range(1, int(input()) + 1):
    # 10 <= N <= 100, 1 <= M, weight, price <= 20
    N, M = map(int, input().split())

    present = [list(map(int, input().split())) for _ in range(M)]
    DP = [[0] * (N + 1) for _ in range(M + 1)]

    for item in range(1, M + 1):  # 각 아이템
        # 현재 아이템의 무게와 가치
        weight, value = present[item - 1][0], present[item - 1][1]

        for bag_size in range(1, N + 1):  # 가방 무게
            if weight <= bag_size:  # 1. 현재 item을 넣을 수 있음
                # max(무게 맞춰서 현재 item 추가한 가치 vs 현재 무게 기준 이전 item까지만큼의 최대 가치) #
                DP[item][bag_size] = max(DP[item - 1][bag_size - weight] + value, DP[item - 1][bag_size])

            else:  # 2. 현재 item을 넣을 수 없음(넣으면 무게 초과)
                # 현재 무게 기준 이전 item까지만큼의 최대 가치
                DP[item][bag_size] = DP[item - 1][bag_size]

    # pprint(DP, width=60)  ###
    print(f'#{tc} {DP[M][N]}')

'''
1
12 5
7 20
3 10
5 3
3 8
6 15

  0  1  2  3  4  5  6  7  8  9 10 11 12
0 x  x  x  x  x  x  x  x  x  x  x  x  x
1 x  0  0  0  0  0  0 20 20 20 20 20 20
2 x  0  0 10 10 10 10 20 20 20 30 30 30
3 x  0  0 10 10 10 10 20 20 20 30 30 30
4 x  0  0 10 10 10 18 20 20 20 30 30 30
5 x  0  0 10 10 10 18 20 20 25 30 30 33

   W   V   item W ~ V
1 [7, 20]= [0][0 ~ 1]
2 [3, 10]= [1][0 ~ 1] 
3 [5, 3]=  [2][0 ~ 1]
4 [3, 8]=  [3][0 ~ 1]
5 [6, 15]= [4][0 ~ 1]
'''
