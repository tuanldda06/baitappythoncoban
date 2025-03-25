#Giải phương trình bậc nhất và bậc hai (Có xử lý ngoại lệ đầu vào)
#Input:Gồm hai dòng:
#Dòng đầu tiên chứa số 1 hoặc 2 tương ứng với:
#Chức năng 1: giải phương trình bậc nhất
#Chức năng 2: giải phương trình bậc hai
#Dòng thứ hai chứa hệ số tùy thuộc vào chức năng được chọn ở dòng 1:
#Chức năng 1: chứa hai số a, b lần lượt là hệ số của phương trình ax + b = 0, các hệ số cách nhau bởi khoảng trắng.
#Chức năng 2: chứa ba số a, b, c lần lượt là hệ số của phương trình ax2 + bx + c = 0, các hệ số cách nhau bởi khoảng trắng.
#Output:Gồm nhiều dòng hiển thị tùy theo các trường hợp như sau:
#Nếu phương trình vô nghiệm: Phuong trinh vo nghiem
#Nếu phương trình có vô số nghiệm: Phuong trinh co vo so nghiem
#Nếu phương trình có một nghiệm duy nhất: Phuong trinh co mot nghiem duy nhat: x = {x1}
#Nếu phương trình có nghiệm kép: Phuong trinh co nghiem kep: x1 = x2 = {x1}
#Nếu phương trình có hai nghiem phan biet: Phuong trinh co hai nghiem phan biet: x1 = {x1} , x2 = {x2}
#Với {x1}, {x2} là các nghiệm của phương trình
#Lưu ý: 
#Nếu dòng đầu tiên khác ‘1’ và ‘2’ thì xuất thông báo: Vui long chon mot trong hai chuc nang : 1. Giai phuong trinh bac nhat 2. Giai phuong trinh bac hai                                                                                                                      
#Nếu file input không tồn tại thì xuất thông báo: Khong tim thay file input!
#Nếu input nằm ngoài định dạng đầu vào thì xuất thông báo: Dinh dang dau vao khong hop le!
import math 
try :
  with open('Bai24.1.inp' ,'r') as fileInp :
    dongdautien = fileInp.readline().split()# dùng readline() để đọc tửng dòng còn split() dùng loại bỏ hết các kí tự xuống dòng(\n)
    thongbao = ""# khởi tạo biến mặc định
    if dongdautien == '1':
      a,b= map(float , fileInp.readline().split())
      if a ==0 :
        if b ==0 :
          print('Phuong trinh co vo so nghiem')
        else :
          print('Phuong trinh vo nghiem')
      else :
        x = -b /a
        print(f'Phuong trinh co nghiem duy nhat: \nx = {round(x,3)}')
     elif dongthuhai == '2' :
       a , b , c = map(float , fileInp.readline().split())
       if a == 0 :
         if b ==0:
           if c==0:
             thongbao ='Phuong trinh co vo so nghiem'
           else :
             thongbao ='Phuong trinh vo nghiem'
         else :
           x = -c/b
           thongbao = f'Phuong trinh co nghiem duy nhat : x ={round(x,3)}'
       else :
         denta = b*b - 4*a*c
         if denta > 0 :
           x1 = (-b+sqrt(denta)) / (2*a)
           x2 = (-b-sqrt(denta)) / (2*a)
           thongbao = f'Phuong trinh co 2 nghiem phan biet : \nx1 = {round(x1,3)} \nx2 = {round(x2,3)}'
         elif denta == 0 :
           x = -b / 2*a
           thongbao = f'Phuong trinh co nghiem duy nhat :x = {x}'
         else :
           thongbao = 'Phuong trinh vo nghiem'
      else :
        thongbao  = 'Vui long chon hai chuc nang : \n1. Giai phuong trinh bac nhat  \n2. Giai phuong trinh bac hai '
except FileNotFoundError :
  thongbao = 'Khong tim thay file input!'
except :
  thongbao = 'Dinh dang dau vao khong hop le!'
with open ('Bai24.1.out' , 'w') as fileOut :
  fileOut.write(thongbao)
  print(thongbao)
      
           
