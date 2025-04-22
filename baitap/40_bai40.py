#Kiểm tra n có phải số nguyên tố không. (Với n là số tự nhiên)
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập giá trị n và x từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số thực và số nguyên tương ứng, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n nhỏ hơn hoặc bằng 0. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for để duyệt các số từ 2 đến căn bậc hai của n:
#Sử dụng cấu trúc rẽ nhánh để kiểm tra có phải là ước số của n hay không
#Nếu có một số là ước của n thì:
#Dùng hàm break thoát vòng lặp
#Hiển thị thông báo n không phải là số nguyên tố
#Nếu trong khoảng 2 đến căn bậc hai của n không có số nào là ước của n thì thông báo n là số nguyên tố
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
# Một số nguyên tố là số tự nhiên lớn hơn 1, chỉ chia hết cho 1 và chính nó.
import math 
try :
    n = int(input())
    if n < 0 :
        print('Vui long nhap so tu nhien')
    elif n <2 : # rào trường hợp n = 1
        print('{} khong phai so nguyen to'.format(n))
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                print('{} khong phai so nguyen to'.format(n))
                break # bài này dùng break vì nếu đã biết n chia hết cho một số nào đó (khác 1 và chính nó), thì không cần kiểm tra tiếp nữa – nó chắc chắn không phải số nguyên tố rồi!
        else :
            print('{} la so nguyen to'.format(n))
except :
    print('Dinh dang dau vao khong hop le')

