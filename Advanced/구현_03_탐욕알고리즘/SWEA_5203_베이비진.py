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
        if card[r] and card[r+1] and card[r+2]:
            return True

    return False


for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))

    A, B = lst[0::2], lst[1::2]
    res = 0

    for idx in range(3, 7):
        if babygin(A[:idx]):
            res = 1
            break

        if babygin(B[:idx]):
            res = 2
            break

    print(f'#{tc} {res}')
