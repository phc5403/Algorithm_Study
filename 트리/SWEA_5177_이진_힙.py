class MinHeap:
    def __init__(self):
        # node를 명시적으로 1번부터 이용하기 위해 초기화시 lst[0] = None
        self.lst = []
        self.lst.append(None)

    def add(self, data):
        # node가 존재하지 않을 경우(초기 = [None])
        if len(self.lst) == 1:
            self.lst.append(data)

        else:
            self.lst.append(data)
            # 새로운 노드 추가 한 시점에서 마지막 노드 위치
            current = len(self.lst) - 1

            while current > 1:
                parent = current // 2

                if self.lst[current] < self.lst[parent]:
                    self.swap(current, parent)

                current //= 2

    def swap(self, p, c):
        self.lst[p], self.lst[c] = self.lst[c], self.lst[p]
        return


for tc in range(1, int(input()) + 1):
    # 최소 힙 문제.
    N = int(input())
    input_num = list(map(int, input().split()))

    tree = MinHeap()

    for num in input_num:
        tree.add(num)

    last_node = len(tree.lst) - 1  # 마지막 노드 번호
    res = 0
    while last_node > 1:
        last_node //= 2
        res += tree.lst[last_node]

    print(f'#{tc} {res}')
