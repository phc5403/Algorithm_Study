def babygin(arr):
    card = [0] * 10

    for i in range(len(arr)):
        card[arr[i]] += 1

    # triplet
    for k in range(len(card)):
        if card[k] >= 3:
            return True

    # run
    for r in range(8):
        if card[r] > 0 and card[r+1] > 0 and card[r+2] > 0:
            return True

    return False


for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))

    A, B = lst[0::2], lst[1::2]
    res = 0

    for idx in range(3, 7):
        if babygin(A[:idx]):
            res = 1
            print(f'#{tc} {res}')
            break

        if babygin(B[:idx]):
            res = 2
            print(f'#{tc} {res}')
            break

    # 무승부
    if not res:
        print(f'#{tc} {res}')
        
'''
처음에 WA, Testcase(8/10) 한 번 났었음.
문제를 잘 읽으면 A와 B의 모든 판단 후에 승자를 비교하는것이 아니라,
A → B 차례로 "개별" 판단하다가 누구든 먼저 완성되는 순간 그대로 끝나야함.
'''
