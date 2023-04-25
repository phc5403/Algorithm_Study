def quick_sort(lst, left, right):
    if left < right:
        p = hoare_partition(lst, left, right)

        quick_sort(lst, left, p -1)
        quick_sort(lst, p + 1, right)

    return


# Pivot의 위치를 반환하는 함수
def hoare_partition(lst, L, R):
    pivot = lst[L]
    left = L + 1
    right = R

    while left <= right:
        while left <= right and lst[left] <= pivot:
            left += 1

        while left <= right and lst[right] >= pivot:
            right -= 1

        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]

    lst[L], lst[right] = lst[right], lst[L]

    return right


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N - 1)
    print(f'#{tc} {arr[N//2]}')
    
