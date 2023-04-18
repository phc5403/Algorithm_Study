for tc in range(1, int(input()) + 1):
    flo = float(input())

    res = ""
    cnt, flag = 1, 1

    # 소숫점에 따라 무리수가되어 무한 루프가 될 수 있는데,
    # 문제에서 중단 지점을 명시해줘서 12자리까지 봄
    while 1:
        # 13자리 이상되면 break
        if cnt == 13:
            flag = 0
            break

        flo *= 2
        if flo > 1.0:
            flo -= 1
            res += '1'

        elif flo == 1.0:
            res += '1'
            flag = 1
            break
        else:  # < 1.0
            res += '0'

        cnt += 1

    if flag:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} overflow')
