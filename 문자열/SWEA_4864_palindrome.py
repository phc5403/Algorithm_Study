def palindrome(arr):
    # 주어진 M(회문 범위)에 맞게 arr을 temp로 가공.
    for start in range(len(arr) - M + 1):
        temp, flag = [], True
        for idx in range(start, start + M):
            temp.append(arr[idx])

        # 투 포인터로 회문 검사
        for left, right in zip(range(len(temp)), range(len(temp)-1, -1, -1)):
            if temp[left] != temp[right]:
                flag = False

            elif left > right:
                break

        if flag:
            return temp


TC = int(input())

for tc in range(1, TC + 1):
    # 문제 조건으로 인해 회문은 반드시 1개 존재.
    # 너무 직관적으로 풀어서.. O(n)이 큼..#
    N, M = map(int, input().split())

    lst = [list(input().strip()) for _ in range(N)]

    res = []

    for r in range(N):
        row, col = [], []
        for c in range(N):
            row.append(lst[r][c])
            col.append(lst[c][r])

        res = palindrome(row)
        if res:
            print(f'#{tc} ', end='')
            print(''.join(res))
            break
            
        res = palindrome(col)
        if res:
            print(f'#{tc} ', end='')
            print(''.join(res))
            break
