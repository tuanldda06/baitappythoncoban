#Nhập và kiểm tra ba số a, b, c có là cạnh của một tam giác không?
a,b,c = map(float,input('Nhap so do cua ba canh:').split())
if a+b>c and b+c>a and a+c>b:
  print('{} {} {} la ba canh cua mot tam giac'.format(a,b,c))
else :
  print('{} {} {} khong phai la ba canh cua mot tam giac'.format(a,b,c))
