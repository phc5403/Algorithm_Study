TC = int(input())

for tc in range(1, TC + 1):
    string = input().strip()

    stack = []
    for s in string:
        if not stack:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

    # print(stack)

    print(f'#{tc} {len(stack)}')
