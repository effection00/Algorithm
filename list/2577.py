
a = int(input())
b = int(input())
c = int(input())

new = list(str(a*b*c))
# 20 * 30 * 40
# 문자열 변환  str
#list로 변환 [2, 4, 0, 0, 0]

for i in range(10): # 0~9인 숫자
  count = new.count(str(i)) #new리스트에서 0~9인 문자 개수 세기
  print(count)
