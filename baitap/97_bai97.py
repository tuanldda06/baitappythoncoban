#Viết hàm trả về tuple gồm 2 phần tử là: số tự nhiên n và tuple chứa n số tự nhiên n. (Tham số tự nhiên n)
def khoi_tao(n) :
  tupleCon = tuple(n for _ in range(n))
  tupleKetqua = tuple(n , tupleCon)
  return tupleKetqua
n = int(input())
ketqua= khoi_tao(tupleX)
print(ketqua)
