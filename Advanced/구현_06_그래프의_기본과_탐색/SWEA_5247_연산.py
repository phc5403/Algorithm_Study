for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    limit = 1000001  # 연산의 중간 결과도 항상 백만 이하의 자연수
    visited = [0] * 1000001  # 방문 표시
    cnt = 0

    # 초기 세팅
    stack = [N]
    visited[N] = 1

    while stack:
        slen = len(stack)

        # END
        if visited[M]:
            break

        cnt += 1
        temp = []
        for _ in range(slen):
            num = stack.pop()

            for nxt in (num + 1, num - 1, num * 2, num - 10):
                if 0 < nxt < limit and not visited[nxt]:
                    visited[nxt] = 1
                    temp.append(nxt)

        stack.extend(temp)

    print(f'#{tc} {cnt}')
