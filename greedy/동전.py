n = int(input())
count = 0

coin_list = [500, 100, 50, 10] 
#단위가 다른 단위의 배수이므로 그리디 알고리즘이 가능
for coin in coin_list:
  count += n//coin #몫 
  n %= coin #n에서 coin 나눈 나머지는 다시 n으로

print(count)

