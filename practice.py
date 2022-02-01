n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i]) #input은 기본적으로 문자열 저장, 그래서 각각의 값을 정수값으로 바꿔주는 과정

d = [] #출력할 부분의 리스트임!
for i in range(24):
  d.append(0)

for i in range(n): #번호 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] +=1

for i in range (1,24):
  print(d[i],end=" ")
