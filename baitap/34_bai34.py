#Tính S(n) = 1 - x + x^2/2! - x^3/3! + … - x^(2n-1)/(2n-1)! + x^(2n)/(2n)!
#Định dạng đầu vào Gồm hai dòng:Dòng đầu tiên chứa số thực x ,Dòng thứ hai chứa số tự nhiên n
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập giá trị n và x từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số thực và số nguyên tương ứng, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n âm. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for để duyệt các số từ 1 tới 2n
#Sử dụng cấu trúc rẽ nhánh để xử lý, tính toán theo công thức
#Dùng hàm print() để hiển thị kết quả ra màn hình theo định dạng đầu ra yêu cầu
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
    x = float(input())
    n = int(input())
    if n < 0:
        print('n phai lon hon 0')
    elif n == 0 or x == 0 :
        print(1)
    else :
        ketqua = 1
        giaithua = 1
        for i in range(1,2*n+1):
            giaithua *= i
            if n %2 == 0 :
                ketqua += pow(x,n)/giaithua
            else :
                ketqua -= pow(x,n)/giaithua
        print('{:.5f}'.format(ketqua))
except :
    print('Dinh dang dau vao khong hop le')