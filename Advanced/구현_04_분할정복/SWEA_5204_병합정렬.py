# 1. Divide & Conquer
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    # Divide #
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # List의 크기가 1이 될 때까지 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    # Conquer #
    return merge(left, right)


# 2. Combine
def merge(left, right):
    global cnt

    res = []  # 분할된 List들을 병합
    le, ri = 0, 0  # left, right의 Index
    lelen, rilen = len(left), len(right)

    if left[-1] > right[-1]:
        cnt += 1

    # 양쪽 List에 원소가 남아있는 경우
    while le < lelen and ri < rilen:
        if left[le] <= right[ri]:
            res.append(left[le])
            le += 1

        else:
            res.append(right[ri])
            ri += 1

    # left가 남아있는 경우
    while le < lelen:
        res.append(left[le])
        le += 1

    # right가 남아잇는 경우
    while ri < rilen:
        res.append(right[ri])
        ri += 1

    return res


for tc in range(1, int(input()) + 1):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))

    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')
