#Viết chương trình giải phương trình bậc nhất và phương trình bậc hai với các hệ số được nhập từ file input và kết quả được xuất ra file output (Có xử lý ngoại lệ đầu vào)
#Định dạng đầu vào :Gồm hai dòng:
#Dòng đầu tiên chứa số 1 hoặc 2 tương ứng với:
#Chức năng 1: giải phương trình bậc nhất
#Chức năng 2: giải phương trình bậc hai
#Dòng thứ hai chứa hệ số tùy thuộc vào chức năng được chọn ở dòng 1:
#Chức năng 1: chứa hai số a, b lần lượt là hệ số của phương trình ax + b = 0, các hệ số cách nhau bởi khoảng trắng.
#Chức năng 2: chứa ba số a, b, c lần lượt là hệ số của phương trình ax2 + bx + c = 0, các hệ số cách nhau bởi khoảng trắng.
#Thuật toán:
#Giải phương trình bậc nhất:
#Phương trình vô số nghiệm khi: hệ số a, b đều bằng 0
#Phương trình vô nghiệm khi: hệ số a bằng 0 và b khác 0
#Các trường hợp còn lại phương trình có nghiệm duy nhất
#Giải phương trình bậc hai:
#Phương trình vô số nghiệm khi: hệ số a, b, c đều bằng 0
#Phương trình vô nghiệm khi: hệ số a, b bằng 0, c khác 0 và trường hợp delta nhỏ hơn 0
#Phương trình có nghiệm kép khi delta bằng 0
#Phương trình có hai nghiệm phân biệt khi delta lớn hơn 0
#Lỗi sẽ phát sinh ở lệnh open() nếu file input không tồn tại. Dùng lệnh except bắt lỗi FileNotFoundError và xử lý.
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi và xử lý.
#Sử dụng câu lệnh with với hàm open() và mode='w' nhằm mở file để ghi thông báo lỗi
import math # dùng thư viện sqrt
try :
    with open('Bai23.inp','r') as fileInp:
        dongdautien = fileInp.readline().rstrip()# readline() đọc 1 dòng duy nhất , rstrip() xóa \n ở bên phải
        if dongdautien =='1' :# nếu là phương trình bậc nhất (theo đầu bài)
            dongthuhai = fileInp.readline()
            a,b = map(float , dongthuhai.split())
            if a == 0:
                if b == 0:
                    thongbao = 'Phuong trinh co vo so nghiem'
                else :
                    thongbao ='Phuong trinh vo nghiem'
            else :
                thongbao = 'Phuong trinh co nghiem duy nhat : \nx = {}'.format(-b/a)
        if dongdautien == '2':
            dongthuhai = fileInp.readline()
            a,b,c = map(float , dongthuhai.split())
            if a== 0 :
                if b ==0 :
                    if c == 0:
                        thongbao = 'Phuong trinh co vo so nghiem'
                    else :
                        thongbao = 'Phuong trinh vo nghiem'
                else :
                    thongbao ='Phuong trinh co nghiem duy nhat: \nx = {}'.format(-c/b)
            else :
                denta = b*b - 4*a*c
                if denta > 0:
                     x1 = float((-b + math.sqrt(denta))/(2*a))
                     x2 = float((-b - math.sqrt(denta))/(2*a))
                     thongbao = 'Phuong trinh co nghiem phan biet : \nx = {} \nx = {}'.format(x1,x2)
                elif denta == 0 :
                    x3 = float(-b/(2*a)) 
                    thongbao = 'Phuong trinh co nghiem duy nhat : \nx = {}'.format(x3)
                else :
                    thongbao = 'Phuong trinh vo nghiem'
        else :
            thongbao = 'Vui long chon mot trong hai chuc nang: \n1. Giai phuong trinh bac nhat \n 2. Giai phuong trinh bac hai'
except FileNotFoundError :
    thongbao = 'File khong ton tai'
except :
    thongbao = 'Dinh dang dau vao khong hop le'
with open('Bai24.out','w') as fileOut :
    fileOut.write(thongbao)
with open('Bai24.out','r') as fileOut :
    print(fileOut.read())


            
            
            
            
            
            
            
            




