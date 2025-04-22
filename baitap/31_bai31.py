#Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu (Phần 2). Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.
#Bài này là tam giác ngược (giảm dần)
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập giá trị n từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n nằm ngoài khoảng 1 đến 9. Hiển thị thông báo lỗi nếu có.
#Sử dụng 2 vòng lặp for, 1 vòng để kiểm soát hàng, 1 vòng để kiểm soát cột
#Dùng hàm print() kết hợp với tham số end để xuất kết quả theo định dạng đề bài yêu cầu
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
    n= int(input())
    if n < 1 or n> 9:
        print('n phai nam trong khoang tu 1 den 9')
    else :
        for hang in range(n):
            for cot in range(n-hang , stop = 0 ,step = -1):
                print(cot , end = ' ')
            print()
except :
    print('Dinh dang dau vao khong hop le ')
    
    