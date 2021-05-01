import sys
list = []
for i in range(9): # 9번 반복
    list.append(int(sys.stdin.readline())) #append함수는 list뒤에 수 추가

print(max(list))
print(list.index(max(list))+1)
