# LIS의 길이를 찾는 문제 # 

for tc in range(1, int(input()) + 1):
    input_data = list(map(int, input().split()))
    N = input_data[0]
    lst = input_data[1:]

    # LIS[i] = i로 끝나는 부분 최장 증가 수열의 원소 개수
    LIS = [0] * N  # 0으로 초기화

    for i in range(N):
        LIS[i] = 1  # 현재 원소로 끝나는 부분 최장 증가 수열은 최소 1개
        for j in range(i + 1):
            if lst[j] < lst[i] and LIS[i] < LIS[j] + 1:
                # LIS가 성립되면 LIS[cur] = LIS[prev] + 1개로 늘어남
                LIS[i] = LIS[j] + 1

    print(f'#{tc} {max(LIS)}')
