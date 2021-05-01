num = [] #list 들어갈 곳 선언

for i in range(10): 
    n = int(input()) #10개 숫자 입력
    num.append(n%42) #42나눈 나머지를 num리스트에 넣어줌
print(len(set(num))) #num을 집합타임2으로 변환(중복 없애줌)