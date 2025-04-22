#Hiển thị số đảo ngược của một số tự nhiên n nhập từ bàn phím (Không dùng xử lý chuỗi)
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập giá trị n từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n âm. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp while để lặp với điều kiện n vẫn còn lớn hơn 0:
#Tách từng chữ số bằng cách chia dư n cho 10
#Tính số đảo ngược theo công thức phù hợp
#Chia lấy thương n cho 10
#Dùng hàm print() để hiển thị kết quả ra màn hình.
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
    n = int(input())
    if n < 0 :
        print('n phai lon hon 0')
    else :
        soDaonguoc = 0
        while n > 0 :
            chusocuoi = n % 10
            soDaonguoc = soDaonguoc*10 + chusocuoi
            n = n // 10
        print(soDaonguoc)

        
except ValueError :
    print('Dinh dang dau vao khong hop le')