#Viết hàm với tham số truyền vào là một danh sách. Trả về set các phần tử xuất hiện trong danh sách đã cho.
def xuly(danhsach) :
  setdsach = set(danhsach)
  return setdsach
danhsach = input().split()
ketqua = xuly(danhsach)
print(ketqua)
