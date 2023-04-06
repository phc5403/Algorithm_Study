# Queue
● FIFO(First-In-First-Out)  
→ 큐에 삽입한 순서대로 원소가 저장.  
→ 가장 먼저 삽입된 원소는 가장 먼저 삭제 됨.  

● 활용 예시  
→ 서비스 대기 행렬 등.  

![image](https://user-images.githubusercontent.com/33312417/230315693-822a0632-94c2-4e9a-a17d-19288c24803b.png)
![image](https://user-images.githubusercontent.com/33312417/230315783-38337438-1772-4949-b8a8-cf49c4fa420c.png)
→ Front, Rear의 초깃값 = -1  
→ 대개 front == rear이면 Queue가 비어있다는 의미.  

# ▶ Queue의 종류  
### 1. Linear Queue(선형 큐)  
→ 간단하고 기본적인 형태, **List 사용**  

### 2. Circular Queue(원형 큐)  
→ 선형에서 발전된 형태, 선형 큐의 문제점을 보완. **List 사용**  

### 3. Linked List Queue(연결 큐)  
→ **Linked List(연결 리스트) 형식을 이용**  

### 4. Priority Queue(우선순위 큐)  
→ 연결에서 응용된 형태, **Heap**을 사용하여 구현.  

## ▶ 1. Linear Queue
● 1차원 List로 구현.  
→ front: 저장된 첫 번째 원소의 Index  
→ rear: 저장된 마지막 원소의 Index  

● front, rear    
→ 초기 상태: 모두 -1  
→ 공백 상태: front == rear  
→ 포화 상태: rear == N-1 (크기 N)  

● 구현  
1. createQueue() → 생성  
  a. 초기 공백 큐 생성.
  b. N 크기의 1차원 List 생성.  
  c. front = rear = -1 초기화.  

2. enQueue(itemp) → 삽입  
  a. 마지막 원소 뒤에 새로운 원소를 삽입하기 위해 rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련함.  
  b. 해당 Index에 해당하는 List 원소 Q[rear]에 item을 저장.  

3. deQueue() → 삭제  
  a. 가장 앞에 있는 원소를 삭제하기 위해 front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동함.  
  b. 새로운 첫 번째 원소를 return함으로써 삭제와 동일한 기능을 함.  

4. isEmpty(), isFull() → 상태 확인  
  a. 공백 상태: front == rear  
  b. 포화 상태: rear == N-1  

5. Qpeek() → 검색
  a. 가장 앞에 있는 원소를 검색하여 반환하는 연산.  
  b. 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환.  
  
● 장점  
→ 삽입, 삭제의 처리 속도 빠름.  

● 단점  
→ List의 size를 고정해서 구현할 경우, 사용할 큐의 크기만큼을 미리 확보 해야함으로써 **메모리 낭비** 발생.  
→ 삽입, 삭제를 반복할 경우, List의 앞부분에 활용할 수 있는 공간이 있음에도, **rear = n-1인 상태 = 포화 상태**로 인식함.  

![image](https://user-images.githubusercontent.com/33312417/230321636-88ea1bc4-f9e7-4e3d-86cd-8321cc0b7e10.png)
→ 더 이상의 삽입을 수행할 수 없음.

● 보완
→ Circular Queue로 메모리 절약, Linked List Queue로 메모리 동적 확보.  
→ Python의 List는 동적으로 메모리 사용이 가능하나, **삽입 및 삭제시 복사, 데이터 이동 등의 연산 수행에 많은 시간이 소모됨.**  
→ Queue 라이브러리 사용으로 단점 회피.  

## ▶ 2. Circular Queue  
● Linear의 단점을 보완하기 위해 고안.  
● 1차원 List를 사용하되, 논리적으로 List의 처음과 끝을 연결하여 원형으로 큐를 이룬다고 가정하고 사용함.  

● front, rear  
→ 초기 및 공백 상태: front = rear = 0  
→ front, rear의 위치가 List의 마지막 Index인 N-1를 가리킨 후, 논리적 순환을 이루어 List의 처음 Index인 0으로 이동해야 함.  
이를 위해 mod(%)를 사용함.  
→ 공백 및 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 **사용하지 않고 항상 빈 자리로 둠.**  

→  Linear와 Circular 큐의 삽입 & 삭제 위치  
Index   |       삽입 위치       | 삭제 위치     
선형 큐 | rear += 1             | front += 1  
원형 큐 | rear = (rear + 1) % N | front = (front + 1) % N  

● 구현  
1. createQueue() → 생성  
  a. 초기 공백 큐 생성.
  b. N 크기의 1차원 List 생성.  
  c. front = rear = 0 초기화.  

2. enQueue(item) → 삽입  
  a. 마지막 원소 뒤에 새로운 원소를 삽입하기 위해 rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함: rear = (rear+1) % N  
  b. Index에 해당하는 List 원소 Q[rear]에 item을 저장  
  
3. deQueue() → 삭제  
  a. 가장 앞에 있는 원소를 삭제하기 위해 front 값을 조정하여 삭제할 자리를 준비함.  
  b. 새로운 front 원소를 return 함으로써 삭제와 동일한 기능을 함.  
  
4. isEmpty(), isFull() → 상태 확인  
  a. 공백 상태: front == rear  
  b. 포화 상태: 삽입할 rear의 다음 위치 == front  
  → (rear + 1) % N == front  
  
● Python으로 구현 했을 경우  
→ 크기를 동적으로 변경할 수 있음 = 메모리 절약  
→ **삽입 및 삭제 시 복사, 데이터 이동 연산을 수행하는데 많은 시간 소요.**  
→ front는 List의 맨 앞 = -1  
→ rear는 List의 맨 뒤 = len(Q) - 1

## ▶ 3. Linked List Queue 
● Linear, Circular의 단점을 보완하기 위해 고안.  
● 단순 연결 리스트를 이용한 Queue.  
  → 큐의 원소: 단순 연결 리스트의 노드  
  → 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있음  
  → front: 첫 번째 노드를 가리키는 링크  
  → rear: 마지막 노드를 가리키는 링크  
  
● 상태 표현  
  → 초기 및 공백 상태: front == rear == None
  → 계속해서 노드를 추가시킬 수 있는 연결리스트의 특징 때문에 포화 상태가 따로 없음.  
  → front와 rear는 각각 Queue의 맨 앞, 맨 뒤의 노드를 가리킴  
  
● 주요 연산 과정  
![image](https://user-images.githubusercontent.com/33312417/230330974-68fe9ffb-9ec6-45a6-95a1-67345a757a1f.png)

![image](https://user-images.githubusercontent.com/33312417/230331349-b1d8678c-f029-48a9-975b-c2e2f59ed791.png)

![image](https://user-images.githubusercontent.com/33312417/230331429-8f523b6c-4234-4c6a-8c50-44f37dfed2ee.png)

● 구현  
1. createLinkedQueue() → 생성  
  a. List Node 없이 포인터 변수만 생성함  
  b. front = rear = None으로 초기화  

2. enQueue(item) → 삽입  
  a. 새로운 노드 생성 후 데이터 필드에 item 저장  
  b. 연결 큐가 공백인지 아닌지에 따라 front, rear 변수 지정  
  `def enQueue(item):  # 연결 큐의 삽입 연산`  
  `    global front, rear`  
  `    newNode = Node(item)  # 새로운 노드 생성`  
  `    if isEmpty():  # 1. 큐가 비어있다면`  
  `        front = newNode`  
  `    else:  # 2. 큐가 비어있지 않다면`  
  `        rear.next = newNode`  
  `    rear = newNode`  

3. deQueue() → 삭제  
  a. old 변수로 지울 노드를 가리키게 하고, front 재설정.  
  b. 삭제 후 공백 큐가 되는 경우 → rear = None  
  c. old가 가리키는 노드를 삭제하고 메모리 반환.  

4. IsEmpty() → 상태 확인  
  → 공백 상태: front == rear == None  
  
● Queue 모듈에 정의된 클래스  
1. `queue.Queue(maxsize)`: FIFO 큐 객체 생성  
2. `queue.LifoQueue(maxsize)`: Stack 개념의 LIFO 큐 객체 생성  
3. `queue.PriorityQueue(maxsize)`: 
  → 우선순위 큐 객체를 생성.  
  → 입력되는 item의 형식 = (순위, item)의 tuple로 입력되며, 우선순위는 숫자가 작을수록 높음.  
※ maxsize는 최대 item 수. 지정하지 않거나 음수일 경우 입력 내용만큼 늘어남.  

● Queue 모듈의 공통 메서드  
1. `qsize()`: 큐 객체에 입력된 item의 개수를 반환.  
2. `put(item[, block[, timeout]])`: 큐 객체에 item을 입력.  
3. `get([block[, timeout]])`: 생성된 큐 객체 특성에 맞추어, item 1개를 반환.  
4. `empty()`: 비어있다면 `return True`  
5. `full()`: 꽉 차있으면 `return True`  
※ 각 클래스의 정렬 방식에 따라 get 계열의 메서드 결과가 달라짐!  


# ▶ Queue의 활용  
## 1. Priority Queue(우선순위 큐)  
● 우선순위를 가진 항목들을 저장하는 큐  

● FIFO가 아니라, **우선순위가 높은 순서대로** 먼저 나가게 됨.  

● 대표적인 적용 분야로는 **시뮬레이션 시스템, 네트워크 트래픽 제어, OS의 Task 스케쥴링**등이 있음.  

● List 또는 우선순위 큐 라이브러리로 구현 및 사용 가능.  

● 삽입 및 삭제  
  → 삽입될 원소를 우선순위에 맞는 위치에 삽입.  
  → 우선순위가 가장 높은(가장 앞)원소를 삭제함.  
  
● List를 이용한 우선순위 큐의 구현  
  1. List를 이용하여 자료 저장  
  2. 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조.  
  3. 가장 앞에 최고 우선순위의 원소가 위치하게 됨.  

● 특징  
  1. List를 사용하므로, 삽입 및 삭제시 원소의 재배치가 빈번함 → 시간이 많이 걸림.  
  2. 이를 해결하기 위해 **PriorityQueue 클래스 사용, Heap 자료구조 사용**  

## 2. Buffer(버퍼)  
● 의미  
  → 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역.  
  → <b>Buffering</b>(버퍼링): 버퍼를 활용하는 방식 or 버터를 채우는 동작  

● 자료 구조  
  → 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용  
  → 물리적인 장치의 처리속도 차에서 발생하는 대기시간을 극복하기 위한 방법.  
  → 데이터를 전송하는 동안 일시적으로 저장하는 영역이므로, 순서대로 데이터가 전달되어야 함.  
  → 따라서 FIFO 자료구조인 **큐가 활용** 됨.  

● Buffer 활용 예시 - 키보드 Buffer의 수행 과정  
1. 사용자가 **키보드로 입력**을 수행하면 **키보드 입력 버퍼**에 차례대로 데이터가 저장됨.  
2. 키보드 입력 버퍼에 **Enter 키 입력**이 들어오면, 이를 **프로그램 실행 영역**에 순서대로 전달하여 연산을 수행하게 됨.  

## 3. Breadth First Search(BFS, 너비 우선 탐색)  
● 일반적으로 DFS = Stack, BFS = Queue를 활용함.  
● BFS  
  → 시작점의 인접한 정점들을 모두 차례로 방문한 후, 방문했던 정점을 시작점으로하여 다시 인접한 정점들을 차례로 방문하는 방식.  
  → 인접한 정점들을 탐색한 후, 차례로 너비 우선 탐색을 진행해야 하므로, FIFO 자료구조인 Queue 활용.  
  
  


