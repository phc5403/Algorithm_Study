# Prim #
def mst_prim(graph, start):  # 그래프, 시작 정점
    # print(f'< Prim_Start >')

    # 1. key, parent, visited를 노드 개수만큼 초기화
    key = [float('inf')] * (V + 1)  # parent[]에 저장된 간선의 가중치
    parent = [None] * (V + 1)  # 정점이 트리에 연결될 때 사용된 간선 정보
    visited = [False] * (V + 1)  # 방문 여부

    # 2. 시작 정점의 가중치를 0으로 설정
    key[start] = 0

    # 3. 정점의 개수만큼 반복
    for _ in range(V + 1):
        minIndex = -1
        minValue = float('inf')

        # print(f'진행도 = {key}, {parent}, {visited}')

        # 4. 방문 안한 정점 중 최소 가중치를 가지는 정점 찾기
        for k in range(V + 1):
            if not visited[k] and key[k] < minValue:
                minIndex = k
                minValue = key[k]

        # 5. 최소 가중치 정점 방문 처리
        visited[minIndex] = True

        # 6. 선택 정점의 인접한 정점 탐색
        for node, weight in graph[minIndex]:  # 정점, 가중치
            # 7. 비트리 정점 중, key값보다 더 작은 가중치로 트리에 연결 가능한 경우
            if not visited[node] and weight < key[node]:
                key[node] = weight  # 가중치 갱신
                parent[node] = minIndex  # 트리에서 연결될 부모 정점

    return sum(key)


# Kruskal #
def mst_kruskal(graph):
    # 1. MST를 구성하는 간선들의 집합 (Defalt = [])
    mst = []

    # 2. 하나의 정점만 포함하는 상호배타 집합을 정점의 수 만큼 생성
    # 자신의 부모를 원소로 가짐, 초기에는 자기 자신을 Root로. Cycle 판단용
    parent = [k for k in range(V + 1)]

    # 3. 탐색
    mst_cost = 0  # MST 가중치

    while len(mst) < V:  # 간선의 개수 = 정점의 개수 - 1까지 반복
        temp = graph.pop()  # 최소 가중치 가져오기
        x, y, weight = temp[0], temp[1], temp[2]

        # Cycle 점검(정점 x, y가 같은 집합에 소속되어있는지 확인)
        if Find_Set(parent, x) != Find_Set(parent, y):  # 다른 집합이면
            Union_Set(parent, x, y)  # 부모값을 갱신해 트리를 합침
            mst.append((x, y))  # 트리에 (x, y) 노드쌍 추가
            mst_cost += weight

    return mst_cost


# Union & Find #
def Find_Set(pr, x):
    if pr[x] != x:
        pr[x] = Find_Set(pr, pr[x])

    return pr[x]


def Union_Set(pr, a, b):
    a = Find_Set(pr, a)
    b = Find_Set(pr, b)

    # 편의상 Root값이 큰것이 낮은것의 서브트리가 되도록 설정
    if a < b:
        pr[b] = a
    else:
        pr[a] = b


# Main #
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    '''
    # < 1. Prim > #
    # 사전에 필요한 상호 배타 집합(각 노드별 간선, 가중치 정보)
    edge = [[] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge[n1].append([n2, w])
        edge[n2].append([n1, w])

    # pprint(edge, width=30)
    print(f'#{tc} {mst_prim(edge, 0)}')
    '''

    # < 2. Kruskal > #
    # 사전에 필요한 "모든 간선을 가중치에 따라 오름차순 정렬한 집합"
    edge = [list(map(int, input().split())) for _ in range(E)]

    # 작업시 pop()을 위해 정렬 후 역순으로 배치
    edge.sort(key=lambda x: x[2], reverse=True)
    # print(edge)

    print(f'#{tc} {mst_kruskal(edge)}')
