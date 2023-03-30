TC = int(input())

for tc in range(1, TC + 1):
    pattern = list(input().strip())
    string = list(input().strip())

    p, s = len(pattern), len(string)

    # < Brute-Force 방식 >
    for idx in range(0, s - p + 1):
        if pattern == string[idx: idx + p]:
            print(f'#{tc} {1}')
            break

        if idx == s - p:
            print(f'#{tc} {0}')
