class CompleteBinaryTree:
    def __init__(self):
        # node를 명시적으로 1번부터 이용하기 위해 초기화시 lst[0] = None
        self.lst = [0] * (N + 1)
        self.lst[0] = None

    def add_leaf(self, idx, data):
        self.lst[idx] = data

    def maketree(self):
        k = N

        while k > 1:
            # 이미 값이있는 Leaf node를 찾았을 때.
            if self.lst[k]:  # Parent node에 값을 누적
                self.lst[k // 2] += self.lst[k]
            k -= 1


for tc in range(1, int(input()) + 1):
    # 전체 노드 개수 / Leaf 노드 개수 / 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]

    tree = CompleteBinaryTree()
    for i, d in leaf:
        tree.add_leaf(i, d)

    tree.maketree()
    print(f'#{tc} {tree.lst[L]}')
    
