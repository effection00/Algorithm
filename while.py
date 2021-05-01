while True: #무한루프
    a, b = map(int, input().split()) #묶어서 정수처리
    if a==0 and b==0 : #0이면 끝남
        break
    print(a+b)