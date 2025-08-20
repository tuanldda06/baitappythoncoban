#Viết hàm với tham số truyền vào là một tuple và một giá trị bất kỳ. Trả về tuple vị trí các phần tử của tuple bằng với giá trị tham số truyền vào.
def xuly(tupleX , value) :
  result = []
  for i in range(len(tuplex)) :
    if tupleX[i] == value :
      result.append(i)
  return tuple(result)
tupleX = tuple(input().split())
value = input()
ketqua = xuly(tupleX , value)
print(ketqua)
  
