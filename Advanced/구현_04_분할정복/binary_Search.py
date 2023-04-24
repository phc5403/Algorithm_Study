# 1. 반복을 통한 구현
def bs_repetition(lst, key):  # key에 해당하는 Index를 반환
    start = 0
    end = len(lst) - 1

    while start <= end:
        # mid = start + (end - start) // 2
        mid = (start + end) // 2

        # Success
        if key == lst[mid]:
            return mid

        elif key < lst[mid]:
            end = mid - 1

        else:  # key > lst[mid]
            start = mid + 1

    # Failure
    return -1


# 2. 재귀를 통한 구현
def bs_recursion(lst, low, high, key):  # key에 해당하는 Index를 반환
    # Failure
    if low > high:
        return -1

    else:
        mid = (low + high) // 2

        # Success
        if key == lst[mid]:
            return mid

        elif key < lst[mid]:
            return bs_recursion(lst, low, mid - 1, key)

        else:  # key > lst[mid]
            return bs_recursion(lst, mid + 1, high, key)


# main #
arr = [3, 2, 1, 6, 9, 4, 8, 7, 5]
arr.sort()  # First of all, sorting is required.
find_num = 3

print(f'Before = {arr}')
print(f'Repetition = arr[{bs_repetition(arr, find_num)}] ')
print(f'Recursion = arr[{bs_recursion(arr, 0, len(arr) - 1, find_num)}]')


