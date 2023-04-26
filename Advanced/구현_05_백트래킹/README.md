## ▶ Backtracking (백트래킹)
● 해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아가는 기법.  
● Optimization(최적화), Decision(결정) 문제를 해결할 수 있음.  
● Promising(유망성), Pruning(가지치기) 개념과 관련있음.  

● 결정 문제의 예시  
※ 문제의 조건을 만족하는 해가 존재하는지의 여부를 Yes or No로 나타내는 문제.  

1. 미로 찾기  
  → 입구에서 출구까지 가는 경로가 존재하는지?  
  → 출구까지 가는 경로 중에 최단 경로는?

2. Subset (부분 집합)  
  → 원소의 합이 조건에 맞는 부분 집합이 존재하는지?  
  → (최적화) 원소의 개수가 최대인 부분 집합은 무엇인지?  
  
3. N-Queen  
4. Map coloring  

### 일반적인 백트래킹 알고리즘 
`def backtracking(node):`  
`    if promising(node):`  
`        if there is a solution at node:`  
`            write the solution`  
`        else:`  
`            for n in each child of node: `  
`                backtracking(n)`  

## ▶ Power set(부분 집합)
● 어떤 집합의 공집합과 자기 자신을 포함한 **모든 부분집합**  
● 원소 개수가 n일 경우 모든 부분집합의 개수는 `2^n`  

● 백트래킹을 활용한 Power set  
1. n개의 원소가 들어있는 집합의 `2^n`개의 부분집합을 만들 때,  
  0 or 1의 값을 가지는 n개의 비트열 List 이용  
2. List의 i번째 항목= i번째 원소가 **부분집합에 포함되는지 여부를 표현**  


## ▶ Permutation (순열)
● 알고리즘  
`def permutation(lst, k, n):`  
`    if k == n:`  
`        print(lst)`  
  
`    else:`  
`        check = [False] * n`  
  
`        for i in range(k):`  
`            check[lst[i]] = True`  
``  
`        for i in range(n):`  
`            if not check[i]:`  
`                lst[k] = i`  
`                permutation(lst, k+1, n)`

