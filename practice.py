class calc:
  def __init__(self,first,second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def dif(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result

while True:
  print("---------------------------------------------------")
  print("1. 더하기\n2. 빼기\n3. 나누기\n4. 곱하기\n5. 전원끄기")
  print("---------------------------------------------------")
  menu = int(input ("원하는 항목을 누르세요. "))
  if menu == 5:
    print("계산기를 종료합니다.")
    break
  a,b = map(int,input("숫자를 입력하세요: ").split(" "))
  num = calc(a,b)
  print("---------------------------------------------------")

  if menu == 1:
    print("값:" , num.add())
  elif menu == 2:
    print("값:",num.dif())
  elif menu == 3:
    print("값:", num.div())
  else :
    print("값:", num.mul())


