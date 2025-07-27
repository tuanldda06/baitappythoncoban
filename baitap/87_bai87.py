#Viết hàm với tham số truyền vào là hai danh sách số thực có cùng kích thước.
# Trả về danh sách kết quả bằng cách nhân lần lượt số đầu tiên của danh sách 1 với số cuối cùng của danh sách 2 cho tới hết danh sách.
def nhan_hai_danh_sach(dsach1, dsach2) :
  dsketqua =  []
  for so1,so2 in zip(dsach1 , dsach2[::-1]) :
    dsketqua.append(so1*so2) 
  # hoặc có thể làm luôn : dsketqua =[so1*so2 for so1 , so2 in zip(dsach1, dsach2[::-1])]
  return dsketqua
danhsach1 = input().split()
danhsach2 = input().split()
if len(danhsach1) != len(danhsach2) :
  print('Vui long nhap 2 danh sach co cung do dai')
else :
  dsach1 = list(map(float,danhsach1))
  dsach2 = list(map(float , danhsach2))
  ketqua = xuly(dsach1, dsach2)
  print(*ketqua)

