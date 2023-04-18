# 완전 탐색
# Brute-Force, Exhaustive Search, Generate and test
→ **가능한 모든 경우들을 나열해 보고 확인**하는 기법  
→ 대부분의 문제에 적용 가능  
→ 문제를 해결하기 위한 간단하고 쉬운 접근법  
→ 문제에 포함된 자료(요소, 인스턴스)의 **크기가 작을 경우 유용**  

## ▶ Sequential Search(순차 검색, 완전 검색)
● 모든 요소를 처음부터 끝까지 비교함  
● **최악의 경우 모든 자료들에 대해 비교 작업 수행**  
● 느리지만 안전한 기법  
● 입력의 크기를 작게 해서 빠르게 답을 구할 수 있으므로, **Greedy & DP**를 활용할 수 있다.  
● PS에서, 완전 탐색으로 접근하여 해답 도출 → 성능 개선을 위해 다른 알고리즘 사용  

## Baby-Gin(베이비진) 문제
● Rule
  → 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑음  
  → Run(런) = 3장의 카드가 연속적인 번호를 갖는 경우   
  → Triplete(트리플릿) = 3장의 카드가 동일한 번호를 갖는 경우  
  → Baby-Gin = 6장의 카드가 Run 과 Triplete으로만 구성된 경우  
  EX) 667767: 2 Triplete = Baby-Gin(666, 777)    
  EX) 054060: 1 Run, 1 Triplete = Baby-Gin(456, 000)  
  EX) 101123: 1 Triplete(111), 남은 023은 Run이 아님!, 1 Run(123)이어도 남은 011이 Triplete이 아님!    

## ▶ 조합적 문제
● 많은 문제들이 **Permutation(순열), Combination(조합), Subset(부분 집합)** 등과 같은 Combinatorial Problems(조합적 문제들)과 관련 있음  
● Sequentail Search는 이러한 조합적 문제에 대한 Brute-force.  

## ▶ 1. Permutation(순열)
● 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것  

● `nPr` = 서로 다른 n개 중 r개를 택하는 순열  
  → `nPr` = `n x (n-1) x (n-2) x ... (n - r + 1)` (r번)  

● `nPn` = `Factorial(n)`  

### **Traveling Salesman Problem**(순회 외판원 문제)가 있음.  
  → 여러 도시들이 있고 한 도시에서 다른 도시로 이동하는 비용이 모두 주어짐  
  → 출발 도시에서 시작해서 다른 모든 도시들을 단 한번만 방문하고 출발 도시로 돌아오는 최소 비용의 이동경로를 구하는 문제  
  → 방문할 도시들을 순서대로 나열하면 하나의 경로가 됨  
  → 모든 경로의 수 = `N!`이므로, `N = 12`만 되어도 479,001,600이나 되버림.    

![image](https://user-images.githubusercontent.com/33312417/232734924-e39dce3f-c080-4b2b-9136-9c03092996af.png)


● Lexicographic_Order(사전식 순서)  

● Minimum-exchange requirement(최소 변경을 통한 방법)  
→ Johnson-Trotter 알고리즘  

### Python - Permutation
`import itertools`  
`# 순열`  
`itertools.permutations(반복 가능 객체, integer)  # integer 생략시 반복 가능 객체의 size`  
  
`# 중복 순열`  
`itertools.product(반복 가능 객체, repeat = integer)  # pepeat의 기본값 = 1`  


## ▶ 2. Subset(부분 집합)
● **바이너리 카운팅을 통한 사전적 순서(Lexicographic Order)**    
  → 비트 표현을 이용해서 부분집합을 생성하는 간단한 방법  
#### Binary Counting(바이너리 카운팅)  
● 사전적 순서로 생성하기 위한 가장 간단한 방법
● 원소 수에 해당하는 N개의 비트 열을 이용  
  → 원소의 크기 N에 대응하는 비트리스트를 사용하지 않고, `0 ~ 2^(N-1)`까지의 정수에 저장된 하위 N개의 비트열 사용  
  → 각 비트는 i번째 해당하는 비트로 구분, (`0 <= i <= N - 1`)  
  → i번째 비트 값 = 1이면 i번째 원소가 포함되었음을 의미  
  ![image](https://user-images.githubusercontent.com/33312417/232743139-7c60da5e-fd98-41fd-8e73-29aed00b3eeb.png)


  
### Knapsack problem(배낭 문제)    
● **Greedy, Dynamic programming**를 활용함.  
  → 배낭과 물건들의 집합이 주어지며, 배낭은 무게가 있고, 아이템들은 각각 무게와 가치가 있음  
  → 배낭에 담는 무게의 총합 < 배낭의 무게  
  → 물건의 총합이 배낭의 무게를 초과하지 않으면서, 가치의 합이 최대가 되는 물건들을 선택하는 문제  
  → 자기 자신과 공집합을 포함한 **모든 부분집합(Power set)의 개수는 2^n**
  → 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가.  
    
## ▶ 3. Combination(조합)
● 서로 다른 n개의 원소 중 r개를 **순서 없이** 골라낸 것  
![image](https://user-images.githubusercontent.com/33312417/232743498-d3f76291-e43e-46e1-8a5e-6b526d534c91.png)
→ 마지막 줄은 "재귀적 표현"  

● 재귀적 정의의 표현  
![image](https://user-images.githubusercontent.com/33312417/232744191-ec867d93-deae-478e-83f2-25c7b4e17298.png)


### Python - Combination
`import itertools`  
`조합`  
`itertools.combinations(반복 가능 객체, r= integer  # r= 생략 불가`  
  
`중복 조합`  
`itertools.combinations_with_replacement(반복 가능 객체, r= integer)  # r= 생략 불가`  



  
