class Node:
    def __init__(self, data):
        self.data = data
        self.prev, self.next = None, None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 1. Element 개수
    def size(self):
        return self.size

    # 2. 맨 앞에 추가
    def addtoFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head  # 새로운 노드의 다음 노드로 첫번째 노드를 가리킴

        # 기존에 노드가 있었다면 현재 head의 이전 노드로 새로운 노드를 지정함. (??)
        if self.head is not None:
            self.head.prev = newNode

        # 새로운 노드가 첫번째 노드가 되도록 head 변경
        self.head = newNode
        self.size += 1  # element 개수 증가

        # head가 끝 노드면
        if self.head.next is None:
            self.tail = self.head  # tail값 조정

    # 3. 맨 뒤에 추가
    def addtoLast(self, data):
        newNode = Node(data)

        # 노드가 없다면 맨 앞의 노드를 삽입하는 함수 호출
        if not self.size:
            self.addtoFirst(data)

        else:
            self.tail.next = newNode  # tail의 다음 노드로 새로운 노드 지정
            newNode.prev = self.tail  # 새로운 노드의 이전노드로 tail 지정
            self.tail = newNode  # 마지막 노드 갱신
            self.size += 1

    # 4. 특정 노드(노드 자체를) 찾기
    def node(self, idx):
        # 찾고자하는게 범위 밖이면 -1 return
        if int(self.size <= idx):
            return -1

        # 찾으려는 idx가 전체 노드를 양분했을 때, Left or Right인지 파악
        if idx < int(self.size // 2):  # idx in Left
            tmp = self.head

            for _ in range(idx):
                tmp = tmp.next

            return tmp

        else:  # idx in Right
            tmp = self.tail

            for _ in range(self.size - 1, idx, -1):
                tmp = tmp.prev

            return tmp

    # 5. 특정 위치에 추가
    def add(self, idx, data):
        # 삽입할 index가 0이면 맨 처음에 추가하는 함수 호출
        if not idx:
            self.addtoFirst(data)

        else:
            temp_front = self.node(idx - 1)  # idx 앞의 노드를 temp_front로 지정
            temp_back = temp_front.next  # idx번째 노드를 temp_back로 지정

            newNode = Node(data)  # 새로운 노드 생성
            temp_front.next = newNode  # t_f의 다음 노드로 새로운 노드 지정
            newNode.next = temp_back  # 새로운 노드의 다음 노드로 t_b 지정

            # t_b가 마지막 노드면 t_b의 이전 노드로 새로운 노드 지정
            if temp_back is not None:
                temp_back.prev = newNode

            # (t_b이 마지막 노드가 아니면) 새로운 노드의 이전 노드를 t_f로 지정
            newNode.prev = temp_front
            self.size += 1

            # 추가한 새로운 노드 다음이 None일 경우(마지막)
            if newNode.next is None:
                self.tail = newNode  # tail 조정

    # 6. 노드 출력
    def toString(self):
        if self.head is None:
            return "[]"

        temp = self.head
        string = "["

        while temp.next is not None:
            string += str(temp.data) + ", "
            temp = temp.next

        string += str(temp.data)
        return string + "]"

    # 7. 맨 앞 노드 삭제
    def removeFirst(self):
        temp = self.head  # 처음 노드를 temp로 지정
        self.head = temp.next  # head를 다음 노드로 변경(2번째 노드)

        tmp_data = temp.data  # 삭제할 노드값을 임시 저장
        temp = None

        # 리스트내에 노드가 있다면, head의 이전 노드를 None으로 지정
        if self.head is not None:
            self.head.prev = None

        self.size -= 1
        return tmp_data

    # 8. idx번째 노드 삭제
    def remove(self, idx):
        # 맨 처음 노드를 삭제할꺼면
        if not idx:
            return self.removeFirst()  # 이미 존재하는 해당 함수 호출

        tempfront = self.node(idx - 1)  # 삭제할 노드 앞의 노드를 tp로 지정
        tempremove = tempfront.next  # 삭제할 노드를 임시 변수에 담음

        # 삭제 대상 앞의 노드의 next를 그 다음 노드로 연결(삭제할 노드를 분리)
        tempfront.next = tempfront.next.next

        # 삭제 대상 노드 기준 전후 노드를 연결
        if tempfront.next is not None:
            tempfront.next.prev = tempfront

        # 삭제 대상 노드의 값을 임시 저장
        removedata = tempremove.data

        # 삭제할 노드가 tail이었다면,
        if tempremove == self.tail:
            self.tail = tempfront  # tail 재설정

        # 삭제 대상 노드를 분리
        tempremove = None

        self.size -= 1

        return removedata

    # 9. 맨 뒤 노드 삭제
    def removeLast(self):
        # 이미 구현해놓은 함수로 간단하게 마지막 위치 삭제
        self.remove(self.size - 1)

    # 10. index로 해당 노드의 data 조회
    def get(self, idx):
        temp = self.node(idx)

        if temp == -1:  # 찾고자 하는 값이 없으면 -1 return
            return -1
        else:  # 있으면 해당 노드의 data return
            return temp.data

    # 11. data로 해당 노드의 index 조회
    def indexOf(self, data):
        temp = self.head  # 탐색 대상 노드를 temp로 지정

        index = 0
        while temp.data != data:
            # 함수 입력값의 data와 노드의 data값 비교
            temp = temp.next
            index += 1

            # 노드 끝까지 갔는데 찾지 못하면 -1 반환환
            if temp is None:
                return -1

        # 찾았으면 해당 노드의 인덱스값을 return
        return index


for tc in range(1, int(input()) + 1):
    # 수열의 길이 / 조작 칸 / 반복 횟수
    N, M, L = map(int, input().split())

    lst = doublyLinkedList()

    for i in map(int, input().split()):
        lst.addtoLast(i)

    for _ in range(M):
        oper = input().split()

        if oper[0] == 'I':
            lst.add(int(oper[1]), int(oper[2]))
            # print(f'I = {lst.toString()}')

        elif oper[0] == 'D':
            lst.remove(int(oper[1]))
            # print(f'D = {lst.toString()} ')

        else:  # 'C'
            lst.node(int(oper[1])).data = int(oper[2])
            # print(f'C = {lst.toString()}')

    res = lst.node(L)

    if res != -1:
        print(f'#{tc} {res.data}')

    else:
        print(f'#{tc} -1')
