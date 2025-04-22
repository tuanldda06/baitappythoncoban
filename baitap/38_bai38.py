#Hiển thị tất cả các ước của một số tự nhiên n nhập từ bàn phím
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập giá trị n và x từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số nguyên tương ứng, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n âm. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for để duyệt các số từ 1 đến n:
#Sử dụng cấu trúc rẽ nhánh để kiểm tra có phải là ước số hay không
#Dùng hàm print() và tham số end để hiển thị kết quả ra màn hình theo định dạng đầu ra yêu cầu
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
    n = int(input())
    if n < 0 :
        print('n phai lon hon 0')
    else :
        for i in range(1,n+1) :
            if n % i == 0:
                print(i , end =' ')
except :
    print('Dinh dang dau vao khong hop le')
    
