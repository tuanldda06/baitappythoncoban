#Viết hàm với tham số truyền vào là tuple X, tuple Y, số nguyên dương k. Trả về tuple kết quả bằng cách thêm các phần tử của tuple Y vào vị trí k của tuple X.
def xuly(tupleX , tupleY , k ) :
  tuplekq = tupleX[:k] + tupleY + tupleX[k:]
  return tuplekq
tupleX = tuple(input().split())
tupleY = tuple(input().split())
k = int(input())
ketqua = xuly(tupleX , tupleY , k )
print(ketqua)
