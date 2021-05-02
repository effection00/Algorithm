n= int(input())
for i in range(n): #n번의 ox값
  score = 0
  sum = 0
  a = input()
  for e in a: #문자열 한개씩 나옴
    if e == 'O': #o인 경우
        score = score + 1 #1씩 더함
        sum = sum + score
    else:  #x의 경우
        score = 0
  print(sum)


   
    



