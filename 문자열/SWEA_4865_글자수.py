TC = int(input())

for tc in range(1, TC + 1):
    # set()으로 중복 문자 걸러냄.
    comparison = set(input().strip())
    string = input().strip()

    cnt = [0] * len(comparison)  # 각 문자의 출현 횟수 저장
    comparison = list(comparison)  # Slice를 위해 List로 변환

    for c in range(len(comparison)):
        for s in range(len(string)):
            # 본문에 비교 문자열이 있을 경우 카운팅
            if comparison[c] == string[s]:
                cnt[c] += 1
    # 카운트 된 숫자 중 제일 큰 수 출력
    print(f'#{tc} {max(cnt)}')
