# 8958
n= int(input())
for i in range(n): #n번의 ox값
  score = 0
  sum = 0
  # 8958
  a = input()
  for e in a: #문자열 한개씩 나옴
    if e == 'O': #o인 경우
        score = score + 1 #1씩 더함
        sum = sum + score
    else:  #x의 경우
        score = 0
  print(sum)

#o o x x o o
#1 2 0 0 1 2 = 6
#1 3 3 3 4 6 
#o o o x o o o
#1 2 3 0 1 2 3 = 12 
#1 3 6 6 7 9 12 


   
    



