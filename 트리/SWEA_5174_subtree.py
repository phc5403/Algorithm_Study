class Node:
    def __init__(self, item):
        self.item = item
        self.left, self.right = None, None


def preorder(node):
    global cnt
    cnt += 1

    # EX = {2: [1, 5], 1: [6], 5: [3], 6: [4]}
    # {parent: childs} -> 단말 노드까지 깊게 탐색
    if node in tree:
        while tree[node]:
            preorder(tree[node].pop())

    return


for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    tree = {}

    edge = list(map(int, input().split()))
    for i in range(0, len(edge), 2):
        parent, child = edge[i], edge[i + 1]

        if parent not in tree:
            tree[parent] = [child]
        else:
            tree[parent].append(child)

    cnt = 0
    print(tree)
    preorder(N)
    print(f'#{tc} {cnt}')
    
'''
처음에 문제를 잘못 이해한게, 너무 중의적 표현에 얽매여 있다보니
'노드 N을 루트로 하는 서브 트리에 속한 노드의 개수'를
'노드 N을 루트로 하는, 서브 트리에 속한 노드의 개수'
-> 주어진 트리에서 노드 N을 루트로 하는(기준을 잡은 변경된 트리의) 서브 트리 ~ 로 생각해버려서..
양쪽 서브트리 중 무얼을 말하는건지 혼동이 왔지만 말 그대로 
"각각의 서브트리로 분할 하였을 때, 노드 N이 루트로 만들어지는 그 때의 해당 서브트리"를 일컫는 것;;

'''
