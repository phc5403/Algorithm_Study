from collections import deque

# PASS 후, 구글링 in 더 효율적인 로직.
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())

    # enumerate()로 피자를 넘버링해서 deque에 추가
    pizza = deque(enumerate(list(map(int, input().split())), start=1))

    fire_pit = deque()

    # 처음에 화덕 크기만큼 피자 넣음.
    for _ in range(N):
        fire_pit.append(pizza.popleft())

    while len(fire_pit) > 1:  # 화덕에 남은 피자가 1개일 때까지 반복
        # 화덕에 공간이 남고 and 피자가 남아있다면 화덕에 넣기
        if len(fire_pit) < N and pizza:
            fire_pit.append(pizza.popleft())

        # 치즈량 검사
        idx, cheese = fire_pit.popleft()

        # 치즈 == 0이 되면 화덕에서 뺀 그대로 다음 반복
        if not cheese // 2:
            continue
        
        else:  # 치즈가 남아있다면 맨 뒤로 다시 넣기
            fire_pit.append([idx, cheese // 2])

    print(f'#{tc} {fire_pit[0][0]}')

