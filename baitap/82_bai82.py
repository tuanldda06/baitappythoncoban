#Viết hàm với tham số truyền vào là một danh sách. Trả về danh sách các phần tử xuất hiện duy nhất trong danh sách đã cho.
def xuly(danhsach) :
  phantu = []
  for a in danhsach :
    if danhsach.count(a) == 1 :
      phantu.append(a)
  return phantu
danhsach = input().split()#Nhập chuỗi và tách ngay thành danh sách
if len(danhsach) == 0 :
  print('Danh sach rong')
else :
  ketqua = xuly(danhsach)
  if len(ketqua) == 0 :
    print('Khong co phan tu duy nhat')
  else :
    print(*ketqua)

      
      
    
