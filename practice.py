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

class perfect_calc(calc):
  def div(self):
    result = self.first // self.second
    return result

print("일반 계산기 결과 값")
a = calc(10,5)
print("+",a.add())
print("-",a.dif())
print("%",a.div())
print("*",a.mul())

print("\n상속 계산기 결과 값")
b = perfect_calc(10,5)
print("+",b.add())
print("-",b.dif())
print("%",b.div())
print("*",b.mul())



