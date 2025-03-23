#Giải phương trình bậc hai ( xử lý ngoại lệ đàu vào)
#Input :Gồm một dòng duy nhất chứa ba số a, b, c lần lượt là hệ số của phương trình ax2 + bx + c = 0, các hệ số cách nhau bởi khoảng trắng.
#Output :Gồm nhiều dòng hiển thị tùy theo các trường hợp như sau:
#Nếu phương trình vô nghiệm: Phuong trinh vo nghiem
#Nếu phương trình có vô số nghiệm: Phuong trinh co vo so nghiem
#Nếu phương trình có một nghiệm duy nhất: Phuong trinh co mot nghiem duy nhat: x = {x1}
#Nếu phương trình có nghiệm kép: Phuong trinh co nghiem kep: x1 = x2 = {x1}
#Nếu phương trình có hai nghiem phan biet: Phuong trinh co hai nghiem phan biet: x1 = {x1} , x2 = {x2}
#Lưu ý: Nếu input nằm ngoài định dạng đầu vào thì xuất thông báo: Dinh dang dau vao khong hop le!
#Hàm round(x, 3) làm tròn số x đến 3 chữ số thập phân.
#F-string cho phép nhúng biến hoặc biểu thức vào trong chuỗi bằng {}.
try :
  import math
  a , b ,c= map(float,input('Nhap lan luot ba so a b ,c :').split())
  if a==0:
    if b ==0:
      if c ==0:
        print('Phuong trinh co vo so nghiem')
      else :
        print('Phuong trinh vo nghiem')
    else :
       x = -b/a
       print('Phuong trinh co nghiem duy nhat:')
       print('x={round(x,3)}')
  else :
    delta = b*b - 4*a*c
    if denta >0 :
      x1 = (-b+sqrt(denta))/(2*a)
      x2 = (-b-sqrt(denta))/(2*a)
      print('Phuong trinh co 2 nghiem phan biet:')
      print('x1 = {round(x1,3)}')
      print('x2 = {round(x2,3)}')
    elif denta == 0:
      x = -b / 2*a
      print('Phuong trinh co nghiem kep:')
      print('x = {round(x,3)}')
    else :
      print('Phuong trinh vo nghiem')
except :
  print('Dinh dang dau vao khong hop le!')
     
