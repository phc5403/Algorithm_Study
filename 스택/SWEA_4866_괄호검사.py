TC = int(input())

for tc in range(1, TC + 1):
    string = list(input().strip())

    lst = []
    for s in string:
        if s == '(' or s == ')' or s == '{' or s == '}':
            lst.append(s)

    stack = []
    flag = 1
    for i in lst:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break

        else:  # '}'
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                flag = 0
                break

    if not stack and flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
