## ▶ Tree
● 비선형 구조로, 원소들 간에 1:N의 관계를 가지는 자료구조.  

● 원소들 간에 계층관계를 가지는 계층형 자료구조.  

● 상위 원소에서 하위 원소로 내려가면서 확장되는 나무 모양의 구조.  

● 한 개 이상의 노드로 이루어진 유한 집합  
  → **Root(루트)** : 최상위 Node.  
  → 나머지 Node들 : 0 <= N개의 분리 집합 T1, T2, ... , Tn으로 분리될 수 있음.  
  → 이렇게 재귀적으로 나누어진 T1, T2, ... , Tn은 각각 하나의 트리가 되며, Root의 **SubTree(서브 트리)** 라고 함.    
  
● Tree의 구성 요소  
  1. node(노드) : Tree의 원소  
  2. edge(간선) : node를 연결하는 선, 부모 node와 자식 node를 연결  
  3. Root node : Tree의 시작 node  
  4. Sibling node(형제 노드) : 같은 부모 node의 자식 node들      
  5. Ancestor node(조상 노드) : edge를 따라 root node까지 이르는 경로에 있는 모든 node들   
  6. Descendent node(자손 노드) : Subtree에 있는 하위 level의 node들   
  7. SubTree(서브 트리) : 부모 node와 연결된 간선을 끊었을 때 생성되는 Tree  
  8. Degree(차수) : 특정 node에 연결된 자식 노드의 수  
  9. Tree의 degree : 일반적으로 Tree에 있는 각 node의 degree 중에서 **가장 큰 값**  
  10. Leaf node(단말or리프 노드) : degree = 0인 node || 자식 node가 없는 node  
  11. Depth (깊이 or 높이) : 일반적으로 root 기준 root level = 0으로 시작하여 아래로 갈 수록 + 1   
  12. Tree의 depth(level) : 일반적으로 Tree에 있는 각 node의 depth(level) 중에서 **가장 큰 값**  

## ▶ Binary Tree(이진 트리)
● 모든 node들이 최대 2개의 Subtree(= 자식 node)를 갖는 특별한 형태의 Tree.  
  → 레벨 i에서의 node의 최대 개수 = `2^i개`    
  → 높이 h인 Binary Tree가 가질 수 있는 node의 `최소 개수 = h + 1`, `최대 개수 = 2^(h+1) - 1`   

## Binary Tree의 종류★☆
### 1. Full binary Tree(포화 이진 트리)
● 모든 level(0에서 시작)에 node가 포화상태로 차 있는 Tree.
  → 높이가 h일 때, 최대의 node 개수인 `2^(h+1) - 1`개의 node를 가진 binary tree  
  → root node = 1번으로 하여 2^(h+1) -1번까지 정해진 위치에 대한 node 번호를 가짐  
  
### 2. Complete binary Tree(완전 이진 트리)
● 높이 = h, node = n (2^h <= n < 2(h+1) - 1)일 때, Full binary tree의 node 번호 1부터 n번까지 빈 자리가 없는 이진 트리.  
![image](https://user-images.githubusercontent.com/33312417/232280849-856b3c53-6ee3-4f4e-8eb6-b0ab22c47e36.png)


### 3. Skewed binary Tree(편향 이진 트리)
● 높이 h에 대한, 최소 개수의 node를 가지면서 **한 쪽 방향의 child node만을 가진 binary tree**   
![image](https://user-images.githubusercontent.com/33312417/232280904-9aba2b28-9882-4efa-8869-e2d12b667fb8.png)

## Binary Tree - Traversal(순회) ★★
● Tree의 각 node를 중복되지 않게 모 방문 하는 것.  
● Tree는 비 선형 구조이기 때문에 선형 구조에서와 같이 **선후 연결 관계를 알 수 없음**  

### 1. Pre-order traversal(전위 순회)
● Root → Left → Right  
`def preorder_traverse(T)`  
`    if T:`  
`        visit(T)  # print(T.item)`  
`        preorder_traverse(T.left)`  
`        preorder_traverse(T.right)`  

### 2. In-order traversal(중위 순회)
● Left → Root → Right  
`def inorder_traverse(T)`  
`    if T:`  
`        inorder_traverse(T.left)`  
`        visit(T)  # print(T.item)`  
`        inorder_traverse(T.right)`  

### 3. Post-order traversal(후위 순회)
● Left → Right → Root  
`def postorder_traverse(T)`  
`    if T:`  
`        postorder_traverse(T.left)`  
`        postorder_traverse(T.right)`  
`        visit(T)  # print(T.item)`  

## ▶ Expression Tree(트리의 표현)
### 1. List를 이용한 Binary Tree
● Root = 1번 ~ 레벨 n에 있는 node에 대하여 왼쪽부터 오른쪽으로 2n ~ 2^(n+1) - 1번 까지 Numbering   
● `List[N + 1]` index 1 ~ N = node 번호
● Level i의 최대 node 수 = 2^i, 전체 node 수 = ∑2^i = 2^(h+1) - 1  

● 성질 (0 < i)    
  → i번 node의 parent node = node(i // 2)  
  → i번 node의 left child node = node(2 * i)   
  → i번 node의 right child node = node(2 * i + 1)  
  
### 2. List를 이용한 Skewed binary Tree(편향 이진 트리)
![image](https://user-images.githubusercontent.com/33312417/232283892-ce97a012-2925-411c-aed4-a4aa789dc343.png)

### List를 이용한 Binary Tree 표현의 단점
● 편향 이진 트리의 경우, 사용하지 않는 리스트 원소에 대한 메모리 공간 낭비 발생  
● 이를 보완하기 위해 **연결 리스트** 를 이용하여 트리를 표현 함.  
  → 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로, 일정한 구조의 **단순 연결 리스트** 노드를 사용하여 구현  
  
![image](https://user-images.githubusercontent.com/33312417/232284952-05754c2c-b3e0-4b3f-abad-211a4ff36d2f.png)


## ▶ Binary search Tree(이진 탐색 트리)
● 탐색 작업을 효율적으로 하기 위한 자료구조  
● 모든 원소는 서로 다른 **유일한 key를 가짐**  
● 왼쪽 서브트리 key < 루트 key < 오른쪽 서브트리 key  
● 왼, 오 서브 트리도 이진 탐색 트리임  
  → **중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있음**    
  
● A. 탐색 연산
  1. root에서 시작  
  2. 탐색할 key 값 x를 루트 노드의 key값과 비교  
    → x == root key : 탐색 연산 성공  
    → x < root key : 루트 노드의 왼쪽 서브트리에서 탐색   
    → x > root key : 루트 노드의 오른쪽 서브트리에서 탐색  
  3. 모든 서브트리에 대해서 순환적으로 탐색 연산을 반복  

● B. 삽입 연산  
  1. 먼저 탐색 연산을 수행
    → 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인  
    → 탐색에서 탐색 실패가 경정되는 위치가 삽입 위치가 됨  
  2. 탐색 실패한 위치에 원소를 삽입  

● C. 이진 탐색 트리의 성능
  1. searching, insertion, deletion(탐색, 삽입, 삭제) 연산 시간은 트리의 깊이에 좌우됨  
    → `O(h), h = BST의 깊이`  
  2. 평균의 경우(이진 트리가 균형적으로 생성되어 있는 경우)  
    → `O(log n)`
  3. 최악의 경우(한쪽으로 치우친 경사 이진 트리의 경우)
    → `O(n)` = 순차 탐색과 시간복잡도가 같음  
    
● 검색 알고리즘의 비교
  1. 리스트에서의 순차 검색 = `O(N)`  
  2. 정렬된 리스트에서의 순차 검색 = `O(N)`  
  3. 정렬된 리스트에서의 이진 검색 = `O(log N)`  
  4. 이진 탐색 트리에서의 평균 = `O(log N)`  
    → 최악의 경우 = `O(N)`  
    → **완전 이진트리** 또는 **균형 트리** 로 바꿀 수 있다면 최악의 경우를 없앨 수 있음  
    → 새로운 원소를 삽입할 때 삽입 시간을 줄임 & 평균과 최악의 시간이 같아짐 `O(log N)`  
    
  5. Hash 검색 = `O(1)`  
    → 단, 데이터를 저장할 **추가 저장 공간**이 필요함.  
    
## ▶ Heap(힙)
● 완전 이진 트리를 응용함  
● 완전 이진 트리에 있는 노드 중에서 키값이 **가장 큰 노드 or 가장 작은 노드**를 찾기 위해서 만든 자료구조  
  → Max heap(최대 힙) : 부모 노드의 key값 >= 자식 노드의 key값, 루트 노드 = 키값이 가장 큰 노드(대부분은 '>=' 지만, 상황에 따라 '>'일 수도 있음!)    
  → Min heap(최소 힙) : 부모 노드의 key값 < 자식 노드의 key값, 루트 노드 = 키값이 가장 작은 노드  

● 완전 이진 트리가 아니거나, 중복된 key값이 존재하면 안됨.  

● Heap - 삽입 연산  
  1. 완전 이진 트리를 구성했을 때, 다음으로 비어있는 곳에 임시로 노드 삽입  
  2. 부모 노드의 key값 대소 비교를 통해 자리 교환  
  3. Root까지 반복 비교 후 자리 확정  

● Heap - 삭제 연산  
  →  head에서는 **Root 노드의 원소만을 삭제**할 수 있음  
  →  Root 노드의 원소만을 삭제하여 반환  
  →  Heap의 종류에 따라 **최댓값 또는 최솟값**을 구할 수 있음  
  → 이를 이용하여 **우선순위 큐**를 heap으로 구현할 수 있음  
  
  1. 루트 노드의 원소 삭제  
  2. 마지막 노드를 루트 노드 위치로 이동  
  3. 삽입 노드와 그 자식 노드를 대소 비교하여 자리 맞추어 교환  
  4. 반복
  
