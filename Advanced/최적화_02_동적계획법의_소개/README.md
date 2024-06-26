# 해당 단원의 문제는, 완벽한 이해가 되기 전까지 .py 생성 X

## ▶ 피보나치 수
● 0과 1로 시작하고 **이전의 두 수 합을 다음 항으로**하는 수열.  

`F(0) = 0, F(1) = 1 (Default)`  
`F(n) = F(n-1) + F(n-2) for n >= 2`  
`함수 F의 정의로부터 피보나치 수열의 n번째 항을 반환하는 함수를 재귀적으로 표현`  

● 기본 구조  
`def fibo(n)`  
`    if n < 2: return n`  
`    else: return fibo(n-1) + fibo(n-2)`  

● 문제점  
→ 정수 n이 클수록, **엄청난 중복 호출**  
→ **n >= 2인 모든 n에 대하여, T(n) > 2^(n/2)**  
→ **O(2^n)**  

## ▶ 수학적 귀납법
● 어떤 등식이 모든 N에 대해서 성립함을 보이기 위해서, **가능한 모든 N을 등식에 대입하여 증명할 수 없음**  
● 따라서, 이하의 방법이 필요함  
  1. 주어진 등식이 **N = 1일 때 성립함을 증명**하고, N일 때 성립한다고 가정한 후, **N + 1일 때 성립함을 증명**  

### 수학적 귀납법을 이용한 증명 과정
1. **Induction base (귀납 기본)**: N=1 (혹은 N=0)에 대해 등식이 성립함을 증명  

2. **Induction hypothesis (귀납 가정)**:  임의의 N에 대해 등식이 성립한다고 가정  

3. **Induction step (귀납 단계)**: 등식이 N + 1에 대해서도 성립함을 증명  

### Pigeonhole principle (비둘기 집의 원리)
● N + 1개의 물건을 N개의 상자에 넣을 때, 적어도 **어느 한 상자에는 두 개 이상의 물건**이 들어 있다는 원리  

● 귀류법으로 증명 가능  

## ▶ Memoization (메모이제이션) ★★★
●  컴퓨터 프로그램 실행 시, 이전에 계산한 값을 메모리에 저장해서 중복 계산하지 않도록 하여 **전체적인 실행속도를 빠르게 하는 기술**  
● **동적 계획법**의 핵심이 되는 기술  

### 피보나치 수에 메모이제이션 적용
● fibo(n)의 값을 계산하자마자 저장하면(memoize) **O(n)으로 줄일 수 있음**  

`# memo 리스트를 할당하고, 모두 0으로 초기화`  
`# memo[0] = 0, memo[1] = 1로 초기화`  
`def memo_fibo(n):`  
`    if n >= 2 and memo[n] == 0:`  
`        memo[n] = memo_fibo(n-1) + memo_fibo(n-2)`  
`    return memo[n]`  

● 특징  
1. **추가적인 메모리 공간 필요**  
2. **재귀 함수 호출**로 인한 시스템 호출 스택을 사용하게 되고 **실행 속도 저하 및 Overflow 발생 가능**  

## ▶ Dynamic Programming (동적 계획법)
● Greedy 알고리즘과 같이 **최적화 문제를 해결**하는 알고리즘  

● 최적화 문제: 최적값(최댓값 or 최솟값)을 구하는 문제  
  → 다수가 존재 할 수 있음  

● 작은 부분 문제들의 해들을 구함 → 해를 이용하여 보다 큰 크기의 부분 문제들 해결 → 최종적으로 원래 주어진 문제 해결  

● **완전 검색**을 좀 더 효율적으로 하는 방법  

● **Recursive + Memoization**  

● **점화식**을 찾으면 가능함  

### DP 적용을 위한 사전 요건
● **Overlapping subproblems (중복 부분문제 구조)** + **Optimal substructure (최적 부분문제 구조)**  

#### 1. Overlapping subproblems
● 큰 문제를 이루는 작은 문제들을 먼저 해결하고, 작은 문제들의 최적 해(Optimal Solution)를 이용하여 순환적으로 큰 문제 해결  
  → Recurrence relation(순환적인 관계)를 명시적으로 표현하기 위해서 **수학적 도구인 점화식 사용**  

● 문제의 순환적인 성질 때문에 **이전에 계산되었졌던** 작은 문제의 해가 **더 큰 문제의 해를 구할 때 중복해서 사용됨**  

● 이미 해결된 **작은 문제들의 해들을** 특정 저장 공간(Table)에 저장(= Memoization)  

● 이미 해결된 문제의 해들이 다시 필요할 때마다 **Table을 참조해서 중복된 계산 피함**  

#### 2. Optimal substructure
● **어느 최적화 문제에나 적용되지 않음**  
  → 주어진 문제가 Principle of Optimality(최적화의 원칙)을 만족해야만 DP를 효율적으로 적용 가능  

● Principle of Optimality (최적화의 원칙)  
  → 어떤 문제에 대한 해가 최적일 때, 그 해를 구성하는 작은 문제들의 해 역시 최적이어야 함  
  → DP 자체가 큰 문제의 최적 해를 작은 문제의 최적 해들을 이용하여 구하는 것  
  → 만약, **큰 문제의 최적 해가 작은 문제들의 최적 해들로 구성되지 않는다면** 해당 문제는 **DP 적용 불가능**  
  → 예를 들면, 최장 경로를 구하는 문제는 DP로 해결되지 않음(최적화의 원칙이 적용되지 않아서).  

### 분할 정복 vs 동적 계획법
1. 분할 정복  
  → 큰 문제를 작은 부분 문제들로 분할  
  → 부분 문제를 **재귀적으로 해결**  
  → 부분 문제의 해를 결합(Combine)  
  → EX) 병합 정렬, 퀵 정렬 등  
  → 상향식 ~> 하향식 방법으로 접근  
  
2. 동적 계획법  
  → 부분 문제들의 해는 더 작은 부분 문제들의 해를 공유함  
  → 모든 부분 문제를 한 번만 계산하고 **결과를 저장하여 재사용 함**  
  → 동적 계획법은 부분 문제들 사이에 **의존적 관계가 존재함**  
  → **관계**는 문제마다 다르고, 대부분의 경우 뚜렷이 보이지 않아서 **Implicit order(함축적인 순서)** 라고 함.  
  → 상향식 방법으로 접근  

### DP 적용 절차
1. 최적해 구조의 특성 파악  
  → 문제를 부분 문제로 분할  
  
2. 최적해의 값을 재귀적으로 정의  
  → 부분 문제의 최적해 값에 기반하여 문제의 최적해 값을 정의(with 점화식)    
  
3. 상향식 방법으로 최적해의 값을 계산  
  → 가장 작은 부분 문제부터 해를 구한 뒤 테이블에 저장  
  → 테이블에 저장되어 있는 부분 문제의 해를 이용하여 점차 상위 부분 문제의 최적해 구함(상향식 방법)  
  
### 피보나치 수에 DP 적용
`def fino_dp(n):  # n >= 2`  
`    f[0] = 0`  
`    f[1] = 1`  
  
`    for k in range(2, n + 1):`  
`        f[k] = f[k - 1] + f[k - 2]`
`    return f[n]`  

● 특징  
1. 재귀 방식보다 수행속도가 더 빠름  
  → (재귀 + memoization) 알고리즘과는 달리 여러번 함수 호출이 없음  
  → 반복문을 사용하기 때문에 함수 호출이 발생하지 않음  

2. 계산하는 항의 총 개수: **T(n) = n + 1**  
  → f[0] ~ f[n]까지 단 한 번씩만 계산  

## ▶ 동전 거스름돈 문제와 이항 계수 문제
### 동전 거스름돈 문제
● 1. 중복을 피하기 위해 재귀 알고리즘에 메모이제이션 적용  
`# change: 거스름돈 금액, coin = [6, 4, 1]: 동전 종류`  
`# memo[]: 이미 구한 부분 문제의 해를 저장, -1로 초기화`  
  
`def CoinChange(change):`  
`    if memo[change] != -1:`  
`        return memo[change]`  
  
`    else:`  
`        min = float('inf')`  
`        for k in range(len(coin)):`  
`            if change - coin[k] >= 0:`  
`                res = CoinChange(change - coin[k])`  
`                if min > res: min = res`  
  
`        memo[change] = min + 1`  
`        return memo[change]`  

● 2. DP 접근: 상향식  
`# change: 거스름돈 금액, coin = [6, 4, 1]: 동전 종류`  
`# memo: 이미 구한 부분 문제의 해를 저장`  
`# 0원에 대한 값은 memo[]에 0으로 사전 초기화`    
`def CoinChange_DP(change):`  
`    for N in range(1, change + 1):`  
`        min = float('inf')`  
`        for k in range(len(coin)):`  
`            if N >= coin[k]:`  
`                res = memo[N - coin[k]]`  
`                if min > res: min = res`  
  
`        memo[N] = min + 1`  
`    return memo[change]`  

### 이항 정리
![image](https://user-images.githubusercontent.com/33312417/236774306-6467201d-b7ba-4af4-b3b9-d1fddbc90126.png)


![image](https://user-images.githubusercontent.com/33312417/236774542-c3a4d823-a0f4-4d5f-b6bb-9c4899360d6b.png)

● 파스칼의 삼각형 - 이항 계수를 삼각형 모양의 기하학적 형태로 배열  

![image](https://user-images.githubusercontent.com/33312417/236775052-ae380846-5f30-4365-ba48-72a7de27b7f9.png)

#### 1. 이항 계수를 구하는 알고리즘: 재귀 호출  
● 입력: 음수가 아닌 정수 n, k (n >= k)  
● 출력: 이항 계수 결과 값  

`def bino(n, k):`  
`    if k == 0 or k == n: return 1`  
`    else:`  
`        return bino(n - 1, k - 1) + bino(n - 1, k)`  
→ 다수의 중복 호출 존재  

#### 2. 이항 계수를 구하는 알고리즘: 메모이제이션
`# B: 이미 구한 부분 문제의 해를 저장, -1로 초기화`  
`def bino(n, k):`  
`    if k == 0 or k == n: return 1`  
  
`    if B[n][k] != -1: return B[n][k]`  
`    else:  # 아직 구하지 않은 값이면`  
`        B[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)`  
`        return B[n][k]`  
→ B[r][c] = B[r - 1][c - 1] + B[r - 1][c]  
→ **행 우선** 탐색하는것과 같은 **순서로 계산하면** 의존성에 위배되지 않음  

#### 3. 이항 계수를 구하는 알고리즘: DP, O(N * K)
`# B: 이미 구한 부분 문제의 해를 저장`  
`def bino(n, k):`  
`    for r in range(n + 1):`  
`        for c in range(min(r, k) + 1):`  
`            if c == 0 or c == r: B[r][c] = 1`  
`            else:`  
`                B[r][c] = B[r - 1][c - 1] + B[r - 1][c]`  
  
`    return B[n][k]`    




