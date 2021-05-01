# for문 이해
#list = [1, 2, 3]
#for s in list:
#print(s) 

n = int(input()) #과목 개수
score = list(map(int, input().split()))  #점수 list
sum = 0 
for s in score: #점수리스트 차례로 출력
    sum += s/max(score)*100  #for문으로 최종 sum 출력
print(sum/n)