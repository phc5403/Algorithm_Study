def backtracking(station, visited, cnt):
    global charge, res

    energy = charge[station]

    # Pruning
    if cnt >= res:
        return

    # END: 현재 위치 + 현재 연료로 종점 도달
    if station + energy >= N:
        res = min(res, cnt)  # 교환 횟수 갱신
        return

    # 현 위치에서 소지 에너지로 갈 수 있는 최대 역까지
    for idx in range(station + 1, station + energy + 1):
        if not visited[idx]:
            visited[station] = True
            backtracking(idx, visited, cnt + 1)
            visited[station] = False

    return

'''  
def backtracking(station, cnt):
    global charge, res

    # 현재 에너지 += 현재 역의 충전량
    energy = charge[station - 1]

    # Pruning
    if cnt >= res:
        return

    # END: 현재 위치 + 현재 연료로 종점 도달
    if station + energy >= N:
        res = min(res, cnt)  # 충전 횟수 갱신
        return

    # 현 위치에서 소지 에너지로 갈 수 있는 최대 역까지
    for idx in range(station + 1, station + energy + 1):
        backtracking(idx, cnt + 1)

    return  
'''
  
for tc in range(1, int(input()) + 1):
    NM = list(map(int, input().split()))

    N, charge = NM[0], [-1] + NM[1:]
    v = [-1, True] + [False] * (N - 2)

    res = float('inf')

    # 출발 역, 에너지, 충전 횟수
    backtracking(1, v, 0)  # visited + DFS
#     backtracking(1, 0)  # 직관적 풀이

    print(f'#{tc} {res}')
