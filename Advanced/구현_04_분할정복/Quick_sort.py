# Quick-Sort
def quickSort(lst, left, right):
    if left < right:
        # Pivot의 위치를 반환하는 함수
        # p = Hoare_partition(lst, left, right)
        p = Lomuto_partition(lst, left, right)

        # pivot 위치를 기준으로 양쪽을 분할하여(자신 미포함) 재귀 호출
        quickSort(lst, left, p - 1)
        quickSort(lst, p + 1, right)

    return


# 호어 알고리즘 -> O(N log N) ~ O(N^2)
# 평균적으로 swap을 3배이상 덜 발생시키기 때문에 로무토보다 유리함.
def Hoare_partition(lst, L, R):
    # pivot을 List의 양끝 중에 하는것 보단,
    # 처음 index, 중간 index, 끝 index의 3개의 요소값중 중간값이 효율적임.
    pivot = lst[L]
    left = L + 1
    right = R

    while left <= right:
        # left = pivot보다 큰 값을 찾는 과정
        while left <= right and lst[left] <= pivot:
            left += 1

        # right = pivot보다 작은 값을 찾는 과정
        while left <= right and lst[right] >= pivot:
            right -= 1

        # 2개의 Sub-while()이 끝나고 나면,
        # left = pivot보다 큰 값, right = pivot보다 작은 값을 가리키는 index가 됨.
        # 즉 "left <= right"라면, 피봇을 사이에 둬야하니 lst[left] ←→ lst[right]가 되야 함.
        if left <= right:  # 그래서 두 값을 교환하는 것
            lst[left], lst[right] = lst[right], lst[left]

    # 위의 메인 "while left <= right"의 반복이 종료됐다는 것은
    # left > right, 즉 서로 교차한 상황
    # 현 시점에서 lst[right] < lst[L] < lst[left]로 역전되므로,
    # pivot을 작은값-큰값 사이에 위치시키기 위해 두 값을 서로 교환하면 된다.
    lst[L], lst[right] = lst[right], lst[L]  # Pivot(lst[L]) ←→ lst[right]

    '''
        r l
    3 2 1 6 9 4 8 7 5 → List 원소
    p
    └→ 요런 상태. lst[p]와 lst[r]을 교환하면 pivot은 자연스레 중간값이 됨.
    '1 2 3' 6 9 4 8 7 5
    '''

    # 바로 위에서 pivot과 right값을 교환했으니,
    # 실제 구하고자하는 중간값은 right가 가리키는 곳의 값이니,
    # right를 return한다 (return pivot 아님)
    return right


# 로무토 알고리즘 -> O(N log N) ~ O(N^2)
def Lomuto_partition(lst, L, R):
    pivot = lst[R]
    left = L - 1

    # left = pivot보다 작은 마지막 값
    # right = pivot보다 큰 마지막 값
    for right in range(L, R):
        if lst[right] <= pivot:
            left += 1
            lst[left], lst[right] = lst[right], lst[left]

    # List를 모두 순회하고 나면,
    # left, right의 정의에 의해
    # pivot은 left ~ right의 중간 크기가 되므로 Swap.
    lst[left + 1], lst[R] = lst[R], lst[left + 1]

    return left + 1


# main #
arr = [3, 2, 1, 6, 9, 4, 8, 7, 5]
print(f'Before = {arr}')
quickSort(arr, 0, len(arr)-1)
print(f'After = {arr}')


