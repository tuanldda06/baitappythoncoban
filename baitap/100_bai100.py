#Viết hàm với tham số truyền vào là một tuple bất kỳ. Trả về tuple số phần tử bằng 0 và số ký tự 0 có trong tuple đó.
def xuly(tupleX) :
  soPtu0 = tupleX.count('0')
  soKtu0 = [pTu.count('0') for pTu in tupleX]
  return soPtu0 , soKytu0
tupleX = tuple(input().split())
soPhantu0 , soKytu0 = xuly(tupleX)
print(soPhantu0)
print(soKytu0)
