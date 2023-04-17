def maketree(num):
    global cnt

    if num <= N:
        maketree(num * 2)  # Left child

        # Numbering
        lst[num] = cnt
        cnt += 1

        maketree(num * 2 + 1)  # Right child

    return


for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [0 for i in range(N + 1)]

    # lst[1 ~ N] = 1 ~ N 노드
    # cnt = 해당 노드의 값
    cnt = 1
    maketree(1)

    print(f'#{tc} {lst[1]} {lst[N//2]}')

'''
1. List를 이용한 Binary Tree 성질
(0 < i)
o i번 node의 parent node = node(i // 2)
o i번 node의 left child node = node(2 * i)
o i번 node의 right child node = node(2 * i + 1)
'''
