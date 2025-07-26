#Viết hàm với tham số truyền vào là một danh sách các số thực. Trả về giá trị, số lượng và vị trí xuất hiện của phần tử lớn nhất trong danh sách.
def xuly(danhsachso) :
  giatri = max(danhsachso)
  solan = danhsachso.count(giatri)
  dsvitri=[vt for vt in (0,len(danhsach)) if danhsachso[vt] == giatri]
  danhsach = input().split()
  if len(danhsach) == 0 :
    
