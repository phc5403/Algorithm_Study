from collections import deque

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    pizza = deque([[i] for i in range(1, M + 1)])

    for j, cheese in zip(range(M), list(map(int, input().split()))):
        pizza[j].append(cheese)

    fire_pit = deque()

    # 처음에 화덕 크기만큼 피자 넣음.
    for _ in range(N):
        fire_pit.append(pizza.popleft())

    flag = 0

    while not flag:
        # 화덕 한 바퀴 돌림
        for _ in range(len(fire_pit)):
            fire_pit[0][1] //= 2  # 화덕이 회전하면서 피자의 치즈를 녹임

            if not fire_pit[0][1]:  # 1. 녹은 후 치즈가 없어지면
                # < END > : 화덕에 피자 1개 남으면 종료
                if len(fire_pit) == 1:
                    print(f'#{tc} {fire_pit[0][0]}')
                    flag = 1
                    break
                
                # 2. 화덕에서 뺌
                fire_pit.popleft()
                
                # 3. 화덕에 자리가 생겼고, 남은 피자가 더 있다면 추가
                if pizza:
                    fire_pit.appendleft(pizza.popleft())
                else:
                    continue

            fire_pit.rotate(-1)  # 다음 피자로 화덕 회전
