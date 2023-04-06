TC = int(input())

for tc in range(1, TC + 1):
    expression = list(input().split())

    flag, res = 1, 0
    stack = []

    for s in expression:

        if s.isdigit():
            stack.append(int(s))

        elif s == '.':
            if len(stack) == 1 and expression.index(s) == len(expression)-1:
                res = stack.pop()
            else:
                flag = 0
                break

        else:  # operator
            if len(stack) < 2:
                flag = 0
                break

            else:
                temp = []
                for _ in range(2):
                    temp.append(stack.pop())

                if s == '*':
                    res = temp[1] * temp[0]

                elif s == '/':
                    res = int(temp[1] / temp[0])

                elif s == '+':
                    res = temp[1] + temp[0]

                else:  # '-'
                    res = temp[1] - temp[0]

                stack.append(res)

    if not stack and flag:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} error')
        
