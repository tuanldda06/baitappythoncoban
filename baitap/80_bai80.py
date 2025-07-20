#Viết hàm với tham số truyền vào là một danh sách các số thực. Sắp xếp danh sách theo thứ tự tăng dần (Không sử dụng hàm sắp xếp có sẵn).
def xuly(danhsachso) :
  for i in range(len(danhsachso)) :
    vitrinhonhat = i
    for j in range(i+1,len(danhsachso)) :
      if danhsachso[j] < danhsachso[vitrinhonhat] :
        vitrinhonhat = j
    danhsachso[vitrinhonhat] , danhsachso[i] = danhsachso[i] , danhsachso[vitrinhonhat]
danhsach = input().split()
if len(danhsach) == 0 :
  print('Danh sach rong')
else :
  danhsachso = list(map(float , danhsach))
  xuly(danhsachso)
  print(*danhsachso)
#Cách hoạt động của hàm xuly:
#Hàm sử dụng thuật toán Selection Sort:
#Duyệt qua từng vị trí i trong danh sách.
#Tìm vị trí vitrinhonhat của phần tử nhỏ nhất trong đoạn từ i+1 đến cuối danh sách.
#Hoán đổi phần tử tại i với phần tử nhỏ nhất tìm được.

