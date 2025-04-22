#Tính và hiển thị ra màn hình n giai thừa (n!)
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập giá trị n từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n âm. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for để duyệt các số từ 1 tới n
#Tính tích các số
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
n = int(input())
def tinh_giai_thua(n) :
    if n == 0 or n ==1 :
        return 1
    else :
        giaithua = 1
        for i in range(1,n+1) :
            giaithua *= i
        return giaithua
if n < 0 :
    print('n phai khong am ')
else :
    ketqua = tinh_giai_thua(n)
    print('{}!={}'.format(n,ketqua))




n = int(input())
def tinh_giai_thua(n) : 
    if n == 0 or n ==1 :
        return 1
    else :
        return n * tinh_giai_thua(n-1)
if n < 0 :
    print('n phai khong am ')
else :
    ketqua = tinh_giai_thua(n)
    print('{}!={}'.format(n,ketqua))
    s


