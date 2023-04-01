TC = int(input())

for tc in range(1, TC + 1):
    # find()를 사용하기 위해 List가 아닌 문자열로 생성
    pattern = input().strip()
    string = input().strip()

    pa_len = len(pattern)
    st_len = len(string)
    skip = [_ for _ in range(len(pattern)-1, -1, -1)] + [pa_len]

    jump, find = 0, 0
    idx = pa_len - 1  # 본문 탐색 Index

    while idx < st_len:  # END_1. idx가 본문 범위를 벗어나거나
        if find:  # END_2. 패턴을 찾았을 때 반복문 종료.
            break

        cnt = 0  # 문자 일치 개수 체크

        # zip()으로 문자열과 패턴을 역순으로 탐색
        for s, p in zip(range(idx, -1, -1), range(pa_len-1, -1, -1)):
            # 문자가 일치 할 때 마다 카운팅
            if string[s] == pattern[p]:
                cnt += 1

                # END_3. 패턴이 모두 일치하면 반복문 종료.
                if cnt == pa_len:
                    find = 1
                    break

            else:  # 문자가 일치하지 않는다면,
                # rfind = find()의 역순
                # 불일치 했으나, pattern 내에 있는지 확인
                jump = pattern.rfind(string[s])
                if jump == -1:  # find()는 못 찾으면 -1 반환
                    jump = skip[-1] - cnt  # 그럴 경우 skip의 '다른 문자'로 점프
                else:  # find() 찾으면 해당 문자의 skip값 대로 점프
                    # 패턴내에 문자가 중복될 수 있으므로,
                    # skipr값 - 맞은 개수 만큼을 점프 해야 함.
                    jump = skip[jump] - cnt
                break
        # 한 번의 탐색이 끝나고나면 idx를 jump만큼 이동
        idx += jump

    # (idx-jump) = 마지막 탐색했던 위치(확인용)
    # print(f'#{tc} {find} / {idx-jump}')
    print(f'#{tc} {find}')

'''
[ 로직 해설 ]

1. 패턴의 끝 vs 해당 위치 맞는 본문 idx 역순비교
2-1. 같다 -> cnt + 1로 카운팅
2-2. 다르다 -> 본문글자가 패턴에 존재하는지 skip[]
* jump = skip[index] - 맞은 개수 *
2-2-1. 존재 O -> 현재 위치 + jump만큼 이동
2-2-2. 존재 X-> 현재 위치 + jump만큼 이동

+ 패턴내에 문자 중복있을 때의 skip 설정
A. 중복되도 그냥 skip에 쓴다.
B. skip[Index] - cnt를 해주기 때문에 알맞게 이동함.
'''
