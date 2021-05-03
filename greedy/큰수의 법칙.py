import time
import datetime
start = time.time()


N, M, K = map(int, input().split())
n = list(map(int, input().split())) #입력 숫자

n.sort() #받은 수 정렬
first = n[N-1] #가장 큰수
second = n[N-2] #두번째 큰수

# k+1개씩 반복 
# 2 3 4 5 배열일 경우 3번까지 가능 11번 더하기
# 5 5 5 4 //5 5 5 4 // 5 5 5  
count = int(m/k+1) * k # count 값 정의 first 더해지는 횟수
count += m%(k+1) #위의 카운트 값에 더하기

result = 0 
result += (count) * first
result += (m-count) * second
print(result)

sec = time.time()-start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)

 
   
  
 