#Tính tích của tổng các chữ số chẵn và tổng các chữ số lẻ của một số tự nhiên nhập từ bàn phím.
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Dùng hàm input() để nhập giá trị n từ bàn phím.
#Chuyển giá trị mới nhận được sang kiểu số thực và số nguyên tương ứng, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp n âm. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp while để lặp với điều kiện n vẫn còn lớn hơn 0:
#Sử dụng cấu trúc rẽ nhánh xử lý trường hợp chữ số chẵn và chữ số lẻ để tính tổng cho hợp lý
#Dùng hàm print() để hiển thị kết quả ra màn hình theo định dạng đầu ra yêu cầu
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hìnhTính tích của tổng các chữ số chẵn và tổng các chữ số lẻ của một số tự nhiên nhập từ bàn phím.
try :
    n = int(input())
    if n < 0 :
        print('n phai lon hon 0')
    else :
        tongsochan = 0
        tongsole = 0
        while n > 0 :
            if n % 2 == 0 :
                tongsochan += n % 10
            else : 
                tongsole += n %10
            n = n // 10
        ketqua = tongsole * tongsochan
        print(ketqua)
except :
    print('Dinh dang dau vao khong hop le')
    


