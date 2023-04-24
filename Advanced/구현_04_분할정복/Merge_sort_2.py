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
    res = []  # 분할된 List들을 병합
    le, ri = 0, 0  # left, right의 Index
    lelen, rilen = len(left), len(right)

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


# Main #
arr = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]
print(merge_sort(arr))  # O(N log N)
# List로 구현할 경우, 전 과정에서 자료의 비교 & 이동 연산이 발생 = 비효율적
