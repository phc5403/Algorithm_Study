def Brute_force(string, pattern):  # 원본 문자열, 패턴
    s_length = len(string)
    p_length = len(pattern)

    # 문자열, 패턴의 Index
    s, p = 0, 0

    while s < s_length and p < p_length:
        if string[s] != pattern[p]:
            s -= p
            p = -1

        s += 1
        p += 1

    if p == p_length:  # 검색 성공
        return s - p_length

    else:  # 검색 실패
        return -1
