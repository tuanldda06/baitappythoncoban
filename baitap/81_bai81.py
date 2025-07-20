#Viết hàm với tham số truyền vào là một danh sách các số nguyên dương. Trả về danh sách các phần tử là số nguyên tố.
import math 
def xuly(n) :
  if n < 2 :# Số nguyên tố phải >= 2
    return False 
  else :
    for i in range(2,int((math.sqrt(n)+1)) ) :
      if n % i == 0 :
        return False
    return True
def kiemtradsach(danhsachso) :
  dssonguyento = [so for so in danhsachso if xuly(so)]
  return dssonguyento
danhsach = input().split()
if len(danhsach ) == 0 :
  print('Danh sach rong ')
else :
  try :
    danhsachso = list(map(int, danhsach))
    ketqua = kiemtradsach(danhsachso)
    if len(ketqua) == 0:
      print('Khong co so nguyen to')
    else:
      print(*ketqua)
  except :
    print('Dinh dang dau vao khong hop le')
  
