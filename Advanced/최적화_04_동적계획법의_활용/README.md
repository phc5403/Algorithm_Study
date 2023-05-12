## ▶ Longest Incresing Subsequence (LIS, 최장 증가 수열)
● 어떤 수열이 왼쪽에서 오른쪽으로 나열되어 있으면, 그 나열 순서를 유지하면서 **크기가 점진적으로 커지는 가장 긴 부분 수열을 추출하는 문제**  

● 부분 수열의 요소들이 **연속적 or 비연속적**  
```  python
EX) lst = [3, 2, 6, 4, 5, 1]
→ {3, 4, 5}, {2, 4, 5}같이 비연속적일 수도 있음  
```  
### 방법 ①: 완전 검색 = O(2^n) 
● 수열의 모든 부분 집합 구함 → 해당 부분 집합이 증가 수열인지 판단 → 증가 수열 중 가장 길이가 긴 값을 구함  

● 부분 수열의 길이가 긴 것부터 조사하는 것이 유리함  

#### 알고리즘 구조
``` python
for i in range(N, 0, -1):
    for 길이가 i인 모든 부분 수열 in range(i):
        if 부분 수열중 증가하는 것을 찾은 경우:
            break
```

### 방법 ②: DP = O(n^2)
1. 입력 수열: { A1, A2, A3, ... ,An }    
``` python
idx =  1   2   3   ...  n
lst = [A1, A2, A3, ... ,An]
```
2. LIS(x): { A1, ... ,Ax }에 존재하는 최장 증가 부분 수열의 길이라고 가정  

3. LIS(x)를 LIS(1), LIS(2), ... , LIS(x - 1)과의 관계로 표현  
  → 길이가 x인 수열의 마지막 요소인 Ax가 증가 부분 수열에 **포함되는 경우, 포함되지 않는 경우**로 나누어서 생각  
  → LIS(x)가 Ax를 포함 / 미포함 하는 경우  

3-1. Case1: LIS(x)가 Ax를 포함하지 않음  
  → LIS(x) = LIS(x - 1)  

3-2. Case2: LIS(x)가 Ax를 포함  
  → LIS(x)는 Ax를 포함하는 최장 증가 수열의 길이임  
  → 증가 수열의 관계인 Aj < Ai인 Aj를 찾음(j < i)  
  → j값을 알 수 없으므로 모두 검색해야함  
  → 찾은 최댓값에 1 증가시켜 LIS(x)에 저장(DP List)  
  → 최종적으로 구해진 1 ~ x의 LIS() 중에서 최댓값 추출  
  → 각 요소로 끝나는 부분적인 최장 증가 수열들 중 **가장 긴 수열이 전체 최장 증가 수열**  

#### 알고리즘 구조
``` python
# LIS[x]: arr[x]로 끝나는 최장 증가 수열의 길이를 저장
def LIS_DP():
    for a in range(1, len(arr)):  # 1. 예시는 Index = 1부터 시작임 
        LIS[a] = 1
        for b in range(1, a):  # 2. for문들의 범위는 실제로 { range(N), range(a + 1) }
            if arr[b] < arr[a] and (1 + LIS[b]) > LIS[a]:
                LIS[a] = LIS[b] + 1
                
    return max(LIS)
```
![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/7c09ccd4-e369-4ade-a4ef-8ddc3f4ae420)


### 방법 ③: 이진 탐색 = O(n log n)
● C[]: 길이 k의 증가 수열에 대하여 가장 작은 값을 C[k]에 저장  

● 각 위치에서 C[index]를 갱신하기 위해 이진 탐색 수행  

#### 알고리즘 구조
● 수열의 길이 N 만큼 반복하고, 최대 길이 N에 대한 이진 탐색 수행  

1. 수열의 요소값을 하나씩 읽어와서 C[index] 범위를 벗어나는 값이면 마지막에 추가  

2. 요소값이 C[index] 범위안에 포함되는 값이라면 자기보다 작은값 다음의 위치에 저장함  

3. 요소값이 저장된 위치가 그 요소값으로 끝나는 최장 증가 수열의 길이가 됨.  

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/a3d8075c-a5c0-4e3c-914b-68a1806b0d45)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/c3d0b694-c073-437d-9e49-44914e803cc9)
▶ 1. 맨 처음 8은 왜 C[]에 저장되지 않는가?  
▶ 2. C[3]에 있던 6은 왜 5로 대체 되는가?  


## ▶ 모든 쌍 최단 경로
● 최단 경로는 정점A에서 정점B까지 **직항로가 없는 경우, 가장 빨리 갈 수 있는 경로를 찾는 문제**  

● "모든 쌍" 최단 경로  
  → 모든 도시 사이에 **가장 빨리 갈 수 있는 경로를 찾는 것**  
  → **가중치 포함, 방향성 그래프**  
  → 음의 가중치 허용, 하지만 가중치 합이 음인 사이클은 허용하지 않음  
  → Optimization probelm (최적화 문제): 주어진 문제에 대하여 하나 이상의 많은 해답이 존재할 때, 이 가운데에서 Optimal solution(가장 최적인 해)를 찾는 것  
  
### 방법 ①: 브루트 포스
● 한 정점에서 다른 정점으로의 모든 경로의 길이를 구한 뒤, 그들 중에서 최소 길이를 찾음  

● N개의 정점을 가지는 완전 그래프일 경우 총 경로의 개수= (N - 2)!  

● 비효율적임

### 방법 ②: Dijkstra ★★★
● 리스트 사용: O(n^3) / (모든 정점의 수 n) * (다익스트라-List= O(n^2))  

● 힙-우선순위 큐: O(N * (E log N)) / (모든 정점의 수 n) * (다익스트라-힙= O(E log N)), (N= 정점 수 E= 간선 수)  

### 방법 ③: Floyd-Warshall ★★★
● 모든 쌍 최단 경로를 찾는 DP 알고리즘(DP 적용)  

● Floyd (플로이드): DP를 변형하여 **모든 쌍 최단 경로를 찾는 알고리즘 고안**  

● Warshall (워샬): 그래프에서 모든 쌍의 경로 존재 여부(Transitive closure)를 찾아내는 **DP 알고리즘 제안**    

● 시간복잡도는 다익스트라-List와 동일한 O(n^3), 하지만 매우 간단하며 음의 가중치를 허용하지 않는 다익스트라 알고리즘보다 효율적임  

#### 접근 방법
● **부분 문제들**을 찾아야 함  
  → D ij k = 정점{1, ... , k}만을 경유 가능하게 고려하여, 정점 i로부터 j까지의 모든 경로 중 **최단 경로의 가중치 합**  
  → 경로가 정점 i에서 정점k 까지의 모든 정점들을 반드시 경유해야 하는 것은 아님  
  
  → k ≠ i, j이고 k=0이면 **어떤 정점도 경유하지 않는다는 것을 의미함**  
  
  → 예시) D ij 1= **min(i에서 1를 경유하는 경로, i에서 j로 직접 가는 경로)**  
  → D ij 2= **min(i에서 2를 경유하는 경로, 이전 D ij 1에서 구한 값)** / 단, 전자는 (D i2 1 + D 2j 1)     
  ![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/31f8a9fc-eeb7-48e3-920e-1278efb35cbc)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/211d13bb-f8c7-4e2c-8614-c2bd7c4994e1)


● 예를 들면, 그래프에 정점이 3개 있는 경우 정점A에서 B까지 직접 가는 경로, 정점C를 경유하는 경로들을 비교  

● **경유 가능한 점들을 하나씩 추가**해 나가면서 최단 경로 구하기  

### 알고리즘
``` python
# D[i][j]: i에서 j로 가는 최단 경로 가중치 합
# 최초 D[i][j]에는 간선(i, j)의 가중치 저장, 없다면 INF

def Floyd-Warshall(D):
    for k in range(1, n + 1):
        for i in range(1, n + 1):  # (i != k)
            for j in range(1, n + 1):  # (i != j, j != k)
                D[i][j] = min(D[i][k] + D[k][j], D[i][j])
```
→ 각 k에 대해서 모든 (i, j)쌍에 대해 계산하면 총 n * n * n = N^3회 계산이 이루어지고, 각 계산은 O(1)이 소요됨  

## ▶ Traveling Salesman Problem (TSP, 순회 외판원 문제) ★★★★★★★
● 출발 후 모든 정점들을 한번씩 방문하고 다시 출발지로 돌아오는 문제  

● 적용할 수 있는 대상: **음이 아닌 가중치, 방향성 그래프**  
● 아직 최적의 효율 알고리즘은 없지만, DP를 적용해서 작은 부분 문제의 최적해를 구하고 더 큰 부분 문제의 최적해를 구하는 방법으로 **중복된 작업을 줄일 수 있음**  

### 알고리즘 - DP
1. V = 모든 정점의 집합, A = V의 부분 집합  
![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/c2e56b08-d5bb-4853-8c53-24782cc590fa)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/fcf68fdc-722d-4627-9e63-b342027f4d3f)

▶ 6:00 ~  

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/55ad894a-8193-457b-a7d1-97fda3a8c477)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/12204b96-18da-4ff5-96bc-86ab66df0de7)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/b235511f-9bad-47b6-b431-ad0b5f4c4ad9)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/765d05fc-58a9-495b-b90e-4f7d29fbffa8)

![image](https://github.com/phc5403/Algorithm_Study/assets/33312417/21db02e7-37c8-443d-b1e6-6af01bb0689e)








