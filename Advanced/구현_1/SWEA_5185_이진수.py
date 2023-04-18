'''
그냥 직관적으로 일일이 풀었는데, 더 효율적으로 풀 수 있을 듯
'''

def convert(num):
    lst = []

    for _ in range(4):
        lst.insert(0, num % 2)
        num = num // 2

    return lst


for tc in range(1, int(input()) + 1):
    N, hex_input = input().split()

    binary = []
    hex_matrix = [i for i in range(10, 16)]

    for hx in hex_input:
        if hx.isdigit():
            binary.append(convert(int(hx)))
        else:
            # print(ord(hx) % 65, hex_matrix[(ord(hx) % 65)])
            binary.append(convert(hex_matrix[ord(hx) % 65]))  # 65 ~ 70

    print(f'#{tc} ', end="")
    for x in binary:
        print(*x, sep='', end='')
    print()
