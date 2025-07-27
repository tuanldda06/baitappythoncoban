#Viết hàm với tham số truyền vào là một danh sách các số thực.
# Trả về trung bình cộng và hai danh sách: một danh sách gồm các số nhỏ hơn và một danh sách gồm các số lớn hơn hoặc bằng trung bình cộng của danh sách được truyền vào.
def xuly(danhsachso) :
  tbc = sum(danhsachso) / len(danhsachso) 
  dsbehon =[]
  dslonhon = []
  for i in danhsachso :
    if i < tbc :
      dsbehon.append(i)
    else :
      dslonhon.append(i)
#Hoặc có thể dùng các ngắn gọn hơn
dsbehon = [so for so in danhsachso if so < tbc]
dslonhon = [so for so in danhsachso if so >= tbc]
  return tbc , dsbehon , dslonhon
danhsach = input().split()
if len(dsach) == 0 :
  print('Danh sach rong')
else :
  danhsachso= list(map(float,dannhsach))
  trungbinhcong , dsachbe , dsachlon = xuly(danhsachso)
  print(trungbinhcong)
  print(*dsachbe)
  print(*dsachlon)
  

