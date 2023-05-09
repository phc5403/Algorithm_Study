## ▶ 0-1 배낭 문제(knapsack)★★★★★
● N개의 물건, 각 물건의 무게, 가치, 배낭의 용량이 주어질 때 배낭에 담을 수 있는 물건의 최대 가치를 찾기  
● 단, 배낭에 담은 물건의 무게의 합이 W를 초과하지 말아야 하고, 각 물건은 1개씩만 선택 가능  

### 배낭 문제: ① 완전 검색
● 완전 검색으로 물건들의 집합 S에 대한 **모든 부분집합 구함**  
● 부분집합에 포함된 물건들의 총 무게가 배낭 무게 W를 초과하는 집합들은 버리고, 나머지 집합에서 **총 값이 가장 큰 집합 선택**  
● 부분집합을 생성하는 상태공간 트리를 탐색하는 방법으로 **모든 후보해 탐색**  

``` python
# W: 남은 배낭의 무게, k: 배낭에 넣을 물건(1...n), 방문하는 노드의 높이  
# curValue: 현재까지 담은 물건의 총 가치, maxValue: 최대 가치
# n: 물건의 개수
  
def knapsack(W, k, curValue)  
    global maxValue
  
    if W >= 0:
        if k > n:
            if maxValue < curValue:
                maxValue = curValue 
  
        else:  
            # k번째 물건을 포함= (배낭 무게 - 현재 물건 무게, 다음 물건, 현재까지의 가치 + 현재 물건 가치)  
            knapsack(W - weight[k], k + 1, curValue + value[k])
  
            # k번째 물건을 포함하지 않음= (배낭 무게 변동 없음, 다음 물건, 현재까지의 가치 변동 없음)
            knapsack(W, k + 1, curValue)
```

### 배낭 문제: ② 재귀 + 메모이제이션
``` python
# K[i][W]: 부분 문제의 해(최대 가치)를 저장하기 위한 List, -1로 사전 초기화  
# i: 배낭에 넣을 물건을 나타내는 값(1...n), W: 배낭의 무게  
n: 물건의 개수  
  
def knapsack(i, W):  
    if K[i][W] != -1: return K[i][W]  # 이미 최대가치가 구해진 상황  
  
    # 물건을 안 넣거나 or 못 넣는경우(=배낭 무게 0)  
    if i == 0 or W == 0  
        K[i][W] = 0  
        return K[i][W]  
  
    else:  
        case1 = 0  
        if W >= weight[i]:  # i번째 물건 포함  
            case1 = knapsack(i - 1, W - weight[i]) + value[i]  
  
        case2 = knapsack(i - 1, W)  # i번째 물건 미포함  
  
        K[i][W] = max(case1, case2)  # 두 경우 중 가치가 높은 것  
        return K[i][W]  
```

### 배낭 문제: ③ DP ★★★★★
``` python
# W: 배낭의 무게, i: 배낭에 넣을 물건(1...n)  
# n: 물건의 개수  
  
def knapsack():  
    # i == 0 or w == 0의 사전 초기화  
    for i in range(n + 1):  
        K[i][0] = 0  
    for w in range(W + 1):  
        K[0][w] = 0  
  
    for i in range(1, n + 1):  
        for w in range(1, W + 1):  
            if weight[i] > w  # i번째 물건= 무게 초과로 담지 못함  
                K[i][w] = K[i -1][w]  
  
            else:  # i번째 물건= 담을 수 있음  
                # max(i번째 물건 포함한 가치, i번째 물건 미포함한 가치)  
                K[i][w] = max(K[i - 1][w - weight[i]] + value[i], K[i-1][w])  
    return K[n][W]  
```

▶ 12:00 ~

## ▶ State-Space Tree (상태 공간 트리)의 탐색 ★★
● 문제 해결 과정의 **중간 상태**를 각각 **한 노드로 나타낸 트리**  

● 상태 공간 트리의 3가지 탐색 방법  
  1. DFS: Back-tracking  
  2. BFS  
  3. A* algorithm(최고 우선 탐색, Best-Frist Search)  

### Branch and Bound (분기 한정)
● 상태 공간 트리를 탐색하는 과정에서 최적해를 찾을 가능성이 없다고 판단되면 **가지치기 수행**  

● 지금까지 찾은 가장 좋은 해보다 **더 좋은 해를 찾을 수 있는가**에 대해서 판단  
  → 판단을 위해 **어떤 전략을 사용하는지**에 따라서 **분기 한정의 효율성 좌우**  
  
● 상태 공간 트리의 노드를 방문할 때마다, 그 **노드의 유망성을 판단**하기 위해 **bound(한계치) 계산**  
  → **한계치**: 해당 노드에서 계속 탐색을 수행하면 얻을 수 있는 후보 해답의 최대치  

● 한계치가 지금까지 찾은 최적의 값보다 **좋지 앟으면 유망하지 않다고 판단**  

## ▶ 배낭 문제 풀이의 여러 기법들
### ① 분기 한정 + 가지치기 + DFS (=백트래킹)
● 상태 공간 트리를 구축하여 백트래킹 기법으로 풀이  

● Root 노드에서 왼쪽으로 가면 첫 번째 물건을 배낭에 넣는 경우이고, 오른쪽으로 가면 첫 번째 물건을 배낭에 넣지 않는 경우  

● 트리의 높이(Level) 1에서 왼쪽으로 가면 두 번째 물건을 배낭에 넣는 경우이고, 오른쪽으로 가면 그렇지 않은 경우  

● 계속하여 상태 공간 트리를 구축하면, Root 노드로부터 단말 노드까지의 모든 경로는 해답 후보가 됨  

● Optimization problem (최적의 해를 찾는 문제)의 경우 **검색이 완전히 끝나기 전에는 해답을 알 수 없음**  

● 검색을 하는 과정 동안 항상 그때까지 찾은 최적해를 기억해야(메모리에 저장) 함  

#### 알고리즘(구조) 
``` python
# best: 지금까지 찾은 최대 가치  
# value(v): 노드 v에서의 가치  
  
def checknode(node v):
    # 최대 가치 갱신
    if best < value(v):
        best = value(v)
    
    # ★ 노드 v에서의 유망성 검사(방식이 어려움) ★ #
    if promising(v):
        # 유망하다면, v의 자식노드들을 검사하기 위해 재귀 호출
        for u in v.child:
            checknode(u)
```

### ② BFS
● Recursive(재귀) 알고리즘 작성은 복잡함으로, Queue(대기 열) 사용  

#### 일반적인 BFS 구조
``` python
# qu: 큐
# tree: 상태 공간 트리
# root: Root of Tree

def bfs(tree, root):
    initialize(qu)
    visit(root)
    enqueue(root)
    
    while qu:
        node = dequeue()
        
        for ch in node.child:
            visit(ch)
            enqueue(ch)
```

#### BFS + 분기 한정
● BFS와의 차이는 **방문하는 자식노드의 bound값을 계산해서 가지치기를 수행하는 것**  

``` python
# qu: 큐, tree: 상태 공간 트리, root: Root of Tree
# best: 지금까지 찾은 최대 가치
# value(node): 해당 node의 가치

def bfs_branch_and_bound(tree, root):
    initialize(qu)
    visit(root)
    enqueue(root)
    best = value(root)
    
    while qu:
        node = dequeue()
        
        for ch in node.child:
            # 최대 가치 갱신
            if best < value(ch):
                best = value(ch)
            
            # 최대 bound값 갱신
            if best < bound(ch):
                visit(ch)
                enqueue(ch)
```
→ 위 알고리즘은 백트래킹 기반 DFS보다 좋지 않음(방문 하는 노드의 개수가 더 많음, 영상 예제 기준 12 vs 17)  

### ③ A* algorithm(최고 우선 탐색, Best-Frist Search)
● 주요 절차  
  1. 주어진 노드의 모든 자식노드 탐색  
  2. 유망하면서 확장되지 않은(Unexpanded) 노드 확인  
  3. 가장 좋은 한계치(bound)를 가진 노드 확장  

● 최고 한계치를 가진 노드를 우선 선택하기 위해서 **Priority Queue (우선순위 큐) 사용**  
  → **Heap(힙)을 사용하여 효과적으로 구현**  
  → 최적해를 빨리 찾을수록 가지치기를 효율적으로 수행함으로써 탐색 시간을 줄일 수 있음(BFS에 비해서 탐색 성능이 좋아짐)  
  
#### 알고리즘(구조)  
``` python
# pq: 우선 순위 큐, tree: 상태 공간 트리, root: root of tree
# best: 지금까지 찾은 최대 가치
# value(node): 해당 node의 가치

def best_first_branch_and_bound(tree, root):
    initialize(pq)
    visit(root)
    insert(root)
    best = value(root)
    
    while pq:
        # 우선순위 큐에의해 bound값이 가장 좋은 node를 꺼냄
        node = remove()
        
        # 현재 node의 한계치가 더 좋다면
        if best < bound(node):
            for ch in node.child:  # 자식노드들도 검사
                if best < value(ch):  # 자식 노드의 최대 가치가 더 좋다면
                    best = value(ch)  # 최대 가치 갱신
                    
                if best < bound(ch):  # 자식 노드의 한계치가 더 좋다면 큐에 삽입
                    visit(ch)
                    insert(ch)
    
```
→ BFS보다 우수함(영상 예제 기준 17 vs 11)  

● 단점  
1. 최적해를 빠른 시간에 찾는다고는 보장 못함  
  → 일반적으로 최적해는 상태 공간 트리의 깊은 곳에 존재할 가능성이 높기 때문  
  
2. Node setup(노드 설정) 비용이 큼  
  → 따라서, 최적해를 찾을 가능성이 높은 노드를 평가해서 다음 노드로 가기 위한 비용을 가능한 최소화 해야함  
  
3. 메모리 사용량이 매우 큼  
  → 후보 노드들의 리스트를 저장하기 위해서 많은 메모리가 요구됨  
  
