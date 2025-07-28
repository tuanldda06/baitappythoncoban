#Viết hàm trả về danh sách gồm các phần tử riêng của hai danh sách (Tham số là 2 danh sách).
def phan_tu_rieng(dsach1 , dsach2) :
  ptrieng1 = [pt for pt in dsach1 if pt not in dsach2]
  ptrieng2 = [pt for pt in dsach2 if pt not in dsach1]
  dsptrieng= ptrieng1 + ptrieng2
  return dsptrieng
danhsach1 = input()
dsanhsach2 = input()
ketqua = phan_tu_rieng(danhsach1 , danhsach2) 
print(*ketqua)
