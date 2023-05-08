## ▶ 0-1 배낭 문제(knapsack)★★★★★
● N개의 물건, 각 물건의 무게, 가치, 배낭의 용량이 주어질 때 배낭에 담을 수 있는 물건의 최대 가치를 찾기  
● 단, 배낭에 담은 물건의 무게의 합이 W를 초과하지 말아야 하고, 각 물건은 1개씩만 선택 가능  

### 배낭 문제: ① 완전 검색
● 완전 검색으로 물건들의 집합 S에 대한 **모든 부분집합 구함**  
● 부분집합에 포함된 물건들의 총 무게가 배낭 무게 W를 초과하는 집합들은 버리고, 나머지 집합에서 **총 값이 가장 큰 집합 선택**  
● 부분집합을 생성하는 상태공간 트리를 탐색하는 방법으로 **모든 후보해 탐색**  

`# W: 남은 배낭의 무게, k: 배낭에 넣을 물건(1...n), 방문하는 노드의 높이`  
`# curValue: 현재까지 담은 물건의 총 가치, maxValue: 최대 가치`  
`# n: 물건의 개수`  
  
`def knapsack(W, k, curValue)`  
`    global maxValue`  
  
`    if W >= 0:`  
`        if k > n:`  
`            if maxValue < curValue:`  
`                maxValue = curValue`  
  
`        else:`  
`            # k번째 물건을 포함= (배낭 무게 - 현재 물건 무게, 다음 물건, 현재까지의 가치 + 현재 물건 가치)`  
`            knapsack(W - weight[k], k + 1, curValue + value[k])`
  
`            # k번째 물건을 포함하지 않음= (배낭 무게 변동 없음, 다음 물건, 현재까지의 가치 변동 없음)`  
`            knapsack(W, k + 1, curValue)`  

### 배낭 문제: ② 재귀 + 메모이제이션
`# K[i][W]: 부분 문제의 해(최대 가치)를 저장하기 위한 List, -1로 사전 초기화`  
`# i: 배낭에 넣을 물건을 나타내는 값(1...n), W: 배낭의 무게`  
`n: 물건의 개수`  
  
`def knapsack(i, W):`  
`    if K[i][W] != -1: return K[i][W]  # 이미 최대가치가 구해진 상황`  
  
`    # 물건을 안 넣거나 or 못 넣는경우(=배낭 무게 0)`  
`    if i == 0 or W == 0`  
`        K[i][W] = 0`  
`        return K[i][W]`  
  
`    else:`  
`        case1 = 0`  
`        if W >= weight[i]:  # i번째 물건 포함`  
`            case1 = knapsack(i - 1, W - weight[i]) + value[i]`  
  
`        case2 = knapsack(i - 1, W)  # i번째 물건 미포함`  
  
`        K[i][W] = max(case1, case2)  # 두 경우 중 가치가 높은 것`  
`        return K[i][W]`  

### 배낭 문제: ③ DP ★★★★★
`# W: 배낭의 무게, i: 배낭에 넣을 물건(1...n)`  
`# n: 물건의 개수`  
  
`def knapsack():`  
`    # i == 0 or w == 0의 사전 초기화`  
`    for i in range(n + 1):`  
`        K[i][0] = 0`  
`    for w in range(W + 1):`  
`        K[0][w] = 0`  
  
`    for i in range(1, n + 1):`  
`        for w in range(1, W + 1):`  
`            if weight[i] > w  # i번째 물건= 무게 초과로 담지 못함`  
`                K[i][w] = K[i -1][w]`  
  
`            else:  # i번째 물건= 담을 수 있음`  
`                # max(i번째 물건 포함한 가치, i번째 물건 미포함한 가치)`  
`                K[i][w] = max(K[i - 1][w - weight[i]] + value[i], K[i-1][w])`  
`    return K[n][W]`  

▶ 12:00 ~

## ▶ 상태 공간 트리의 탐색


