#1110번

A = int(input()) #최초값이므로 건들이지 않기 
first = A #시작하는 수
cycle = 0 #count
while True:
  a = first//10  #first의 앞자리
  b = first%10   #first의 뒷자리
  c = (a+b)%10  #합의 뒷자리
  num = (b*10) + c
  cycle = cycle + 1
  if num == A:
    break
  first = num #num의 값이 처음으로 감
print(cycle)
     