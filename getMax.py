from operator import index


li = list(map(int,input("숫자 입력: ").split(" ")))

m = li[0]

def getMax(m):
  for i in li:
    if i > m :
      m = i
  return m

print("최댓값 : ",getMax(m))