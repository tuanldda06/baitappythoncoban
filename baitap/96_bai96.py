#Viết hàm với tham số truyền vào là số tự nhiên n. Khởi tạo và hiển thị tuple chứa n số tự nhiên đầu tiên ra màn hình.
def xuly(n) :
  dsach = []
  for i in range(n) :
    dsach.append(i)
  return tuple(dsach)
n = int(input())
ketqua = xuly(n)
print(ketqua)
