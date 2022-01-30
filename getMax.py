li = list(map(int,input("숫자 입력 :").split(" ")))

m = li[0] #m이라는 변수에 최댓값 저장할 것임.

def getMax(m):
  for i in li: 
    if i > m : #m[0]값이랑 li 전체를 비교(for문 한바퀴 돌림)
      m = i # 이 때 m값이 더 크면 그냥 넘어가고 i가 더 클 경우 m이랑 i값 같게 설정
  return m

print(getMax(m))