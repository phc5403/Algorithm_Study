from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    container = deque(sorted(map(int, input().split()), reverse=True))
    truck = deque(sorted(map(int, input().split()), reverse=True))

    res = 0

    for t in truck:
        for c in container:
            if t >= c:
                res += c
                container.remove(c)
                break

    print(f'#{tc} {res}')
    
