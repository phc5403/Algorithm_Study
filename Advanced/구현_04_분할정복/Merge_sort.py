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
    result = []  # 분할된 List들을 병합

    # 양쪽 LIst에 원소가 남아있는 경우
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))

        else:
            result.append(right.pop(0))

    # left가 남아있는 경우
    if left:
        result.extend(left)

    # right가 남아잇는 경우
    if right:
        result.extend(right)

    return result


# Main #
arr = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]
print(merge_sort(arr))  # O(N log N)
# List로 구현할 경우, 전 과정에서 자료의 비교 & 이동 연산이 발생 = 비효율적
