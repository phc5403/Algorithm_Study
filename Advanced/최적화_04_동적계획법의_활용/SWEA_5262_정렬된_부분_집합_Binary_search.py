def binary_search(num, right):  # 자리 찾을 숫자, 현재 LIS[]의 마지막 index
    left = 0

    # 이분 탐색
    while left < right:
        mid = (left + right) // 2

        if LIS[mid] < num:
            left = mid + 1

        else:  # LIS[mid] >= num
            right = mid

    return right


for tc in range(1, int(input()) + 1):
    input_data = list(map(int, input().split()))
    N = input_data[0]
    lst = input_data[1:]

    # LIS[k]= 길이가 k인 LIS, 길이 0은 작은수로 초기화
    LIS = [float('-inf')] + [0] * (N - 1)

    i, j = 0, 0  # lst, LIS의 index
    while i < len(lst):  # 수열 전체 순회
        # 1. List의 숫자가 구해놓은 LIS의 마지막 숫자보다 큰 경우 = LIS 성립
        if LIS[j] < lst[i]:
            LIS[j + 1] = lst[i]  # LIS[다음 위치]값 갱신
            j += 1  # LIS의 마지막 위치를 가리키도록 함
        
        # 2. List의 숫자가 새로 들어갈 위치를 찾기
        else:  # LIS[j] >= lst[i]
            idx = binary_search(lst[i], j)  # 이분 탐색
            LIS[idx] = lst[i]  # 새 위치로 갱신 

        i += 1  # 다음 요소 검색
      
    # while()이 끝나고 나면, LIS 리스트가 완성됨
    # LIS[index] = value ▶ value로 끝나는 LIS의 길이는 index.

    print(f'#{tc} {j}')
