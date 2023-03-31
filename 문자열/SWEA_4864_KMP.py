def route_table(pa, len_pa):
    # 최대 경계 너비 계산 리스트
    # index = 일치하는 패턴의 길이
    # temp[index] = 최대 경계 너비

    # 0개 ~ 패턴 글자개수 만큼 표시할 공간이 필요함.
    table = [0] * (len_pa + 1)  # 본문과 패턴사이의 일치하는 글자의 개수

    # 일치하는 문자가 0개면 1칸 이동하기 위한 설정
    table[0] = -1

    # 일치하는 패턴의 길이가 문자 1개면, 경계를 찾을 수 없음.
    # => 한글자에는 접두사, 접미사가 없기 때문.
    table[1] = 0

    left = 0
    for right in range(1, len_pa):
        # 마지막으로 같았던 위치로 left 회귀
        # ★☆★☆ 이 부분이 아직 이해가 잘 안감 ★☆★☆
        while left > 0 and pa[left] != pa[right]:
            left = table[left]

        # 일치하면 위치 기록
        if pa[left] == pa[right]:
            # left의 위치 기준, 그 전까지는 경계가 일치한다는 뜻이므로
            # left를 한 칸 다음으로 옮겨줌
            left += 1

            # 패턴 문자열의 idx(right) = 현재 패턴에서 몇 번째 글자를 보는지
            # -> 흔히 배열 탐색처럼 0 ~ len-1의 Index를 가짐.
            table[right + 1] = left
            # 따라서, 실제적으로 글자수 셀 때는 1개, 2개, ... 이므로
            # table[right + 1]이 의미하는 것은
            # 현재 "본문과 패턴사이"에 "right + 1번째 글자까지" 일치한다는 뜻.
    return table


TC = int(input())

for tc in range(1, TC + 1):
    pattern = list(input().strip())
    string = list(input().strip())

    # 1. 이동거리 계산 테이블 생성 #
    nxt = route_table(pattern, len(pattern))

    # string[Index], 이동 거리, 맞은 개수
    idx, move, cnt = 0, 0, 0
    find = 0  # 검색 여부

    # 2. 문자열 비교 #
    # 점프해서 보는 위치 + 패턴 길이만큼 검색해야하는데
    # 그게 본문의 길이가 넘으면 검색 실패(에 맞춰 while 범위 설정)
    while move + len(pattern) <= len(string):
        # 현재 위치(idx) + 이동해서 볼 거리(초기 0)과 pattern 비교
        if string[idx + move] == pattern[cnt]:
            cnt += 1
            idx += 1  # 현재 일치 함 = 다음으로 + 1

            # 패턴의 길이만큼 개수가 일치하면 Find.
            if cnt == len(pattern):
                find = 1
                # print(move)  # 본문의 move번째 글자부터 패턴 일치함.
                break

        else:  # 문자가 다르면
            # 이동거리 = 일치하는 패턴 길이(cnt) - 최대 경계 너비(nxt[cnt])
            move += cnt - nxt[cnt]
            # 다음 검색에는 처음부터(0) + 이동거리(move)의 위치부터 검색하기 위함.
            idx, cnt = 0, 0

    print(f'#{tc} {find}')
