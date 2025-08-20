#Viết hàm với tham số truyền vào là một set bất kỳ. Trả về set rỗng nếu set có chẵn phần tử.
def xuly(setX) :
  if len(setX) % 2 == 0 :
    setX.clear()  #Ham clear() xoa tat ca phan tu trong set
  return setX
danhsach = input().split()
if len(danhsach) == 0 :
  print('Danh sach rong')
else :
  setX = set(danhsach)
  ketqua = xuly(setX)
  print(ketqua)
  

    
