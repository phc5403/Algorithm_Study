# 1. 패턴에 대해 불일치 발생 시 돌아갈 곳을 계산하는 전처리 함수 알고리즘 #
def KMP_preprocess(pattern, nxt):
    # nxt[]를 만드는 과정

    p_lengh = len(pattern)
    nxt = [0] * p_lengh  # 패턴의 길이 만큼 할당

    i, k = 0, -1
    # k = 지금까지 일치한 문자열의 개수

    while i < p_lengh:
        nxt[i] = k  # 첫 글자는 돌아갈 곳이 없으므로 -1

        # 접두어, 접미어를 찾는 과정
        while 0 <= k and pattern[i] != pattern[k]:
            k = nxt[k]

        i += 1
        k += 1

# 2. 전처리 후 문자열 내의 패턴을 탐색하는 알고리즘 #
def KMP_Search(string, pattern, nxt):
    s_length, p_length = len(string), len(pattern)
    s, p = 0, 0

    # 전체 문자열 길이만큼 순회
    while s < s_length:

        # 불일치 발생
        while 0 <= p and string[s] != pattern[p]:
            p = nxt[p]

        s += 1
        p += 1

        if p == p_length:  # 검색 성공
            return s - p  # 문자열에서 패턴의 시작 위치 반환

    return -1  # 검색 실패
