#Nhập và kiểm tra ba số a, b, c có là cạnh của một tam giác không? (Có xử lý ngoại lệ đầu vào)
#Input :Gồm một dòng duy nhất chưa ba số a, b, c cách nhau bởi khoảng trắng.
#Output :Gồm một dòng duy nhất hiển thị như sau:
#Nếu a, b, c là ba cạnh của một tam giác: {a}, {b}, {c} la ba canh cua mot tam giac
#Nếu a, b, c không là ba cạnh của một tam giác: {a}, {b}, {c} khong phai la ba canh cua mot tam giac
#Với {a}, {b}, {c} là ba số nhập vào từ bàn phím
#Lưu ý: Nếu a, b, c là số âm thì xuất thông báo: Cac canh cua tam giac phai lon hon 0!
#Nếu input nằm ngoài định dạng đầu vào thì xuất thông báo: Dinh dang dau vao khong hop le!
try :
  a,b,c = map(float,input('Nhap lan luot ba so la: ').split())
  if a <=0 or b<=0 or c<=0 :
    print('Cac canh cua tam giac phai lon hon 0!')
  elif a+b>c and b+c>a and a+c>b:
    print('{} {} {} la ba canh cua mot tam giac'.format(a,b,c))
  else :
    print('{} {} {} khong phai la ba canh cua mot tam giac'.format(a,b,c))
except :
  print('Dinh dang dau vao khong hop le!')
  

