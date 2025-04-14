#Tính tổng các số nguyên trong khoảng a đến b. (Vòng lặp while)
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập hai giá trị a, b từ bàn phím.
#Chuyển hai giá trị mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp a > b. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for với biến giá trị chạy từ a đến b:
#Thực hiện cộng dồn các giá trị
#Dùng hàm print() hiển thị kết quả cần tính ra màn hình
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
    a = int(input())
    b = int(input())
    if a > b:
        print('a phai lon hon b')
    else :
        tong = 0
        i = a
        while i <= b :
            tong += i
        print(tong)
except :
    print('Dinh dang dau vao khong hop le')

