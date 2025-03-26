#Tính tổng các số nguyên trong khoảng a đến b. (Vòng lặp for)
#Input : Gồm hai dòng :Dòng đầu tiên chứa số nguyên a , dòng thứ hai chứa số nguyên b
#Output :Gồm một dòng duy nhất hiển thị tổng các số trong khoảng từ a đến b
#Lưu ý: 
#Nếu a > b thì xuất thông báo: So thu nhat lon hon so thu hai!
#Nếu input nằm ngoài định dạng đầu vào thì xuất thông báo: Dinh dang dau vao khong hop le!
try :
  a = int(input('Nhap so thu nhat la : '))
  b = int(input('Nhap so thu hai la : '))
  if a > b :
    print('So thu nhat lon hon so thu hai!')
  else :
    tong = 0
    for i in range(a , b+1) :
      tong +=i
      print(f'Tong cac chu so tu {a} den {b} la : {tong}')
except :
  print('Dinh dang dau vao khong hop le!')
  

