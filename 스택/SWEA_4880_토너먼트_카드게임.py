# Divide and Conquer #

def divide(begin, end):

    if begin == end:
        return begin

    mid = (begin + end) // 2

    # mid를 중심으로 조 양분
    left = divide(begin, mid)
    right = divide(mid+1, end)

    # 양분하다가 Left, Right 1명씩 정해지면 대결
    return conquer(left, right)


def conquer(x, y):
    # 비기면 학생 번호가 빠른사람이 이김
    if stu[x] == stu[y]:
        return x

    # x가 이기는 경우
    elif stu[x] - stu[y] == 1 or stu[x] - stu[y] == -2:
        return x

    # y가 이기는 경우
    else:
        return y


TC = int(input())

for tc in range(1, TC+1):
    # 4 <= N <= 100
    N = int(input())
    stu = list(map(int, input().split()))

    print(f'#{tc} {divide(0, len(stu) -1) + 1}')
