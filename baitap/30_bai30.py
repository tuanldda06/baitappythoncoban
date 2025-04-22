#Viết chương trình hiển thị ra màn hình tam giác số kích thước n theo mẫu. Với n là số tự nhiên từ 1 đến 9 nhập từ bàn phím.try:
#Bài này là tam giác thuận(tăng dần)
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
    n = int(input())
    if n < 1 or n > 9 :
        print('n phai nam trong khoang tu 1 den 9')
    else :
        for hang in range(1,n+1) :#Dùng để lặp qua từng hàng ngang hay hang: là số thứ tự của dòng

            print("Đang ở dòng:", hang)
            for cot in range(1,hang+1):#Dùng để in ra từng số trong mỗi hàng hay cot: đại diện cho các số được in ra trong mỗi dòng
                print(cot , end = ' ')#vòng lặp cột – lồng bên trong mỗi dòng.
            print()# Nếu bạn muốn mỗi dòng số được in ra nằm trên một dòng riêng biệt → bạn bắt buộc phải có print() sau vòng lặp bên trong.
except ValueError :
    print('Dinh dang dau vao khong hop le')
# Lồng for để t/m yêu cầu bài toán
#Giả sứ với n = 4 thì sẽ có 4 dòng , và ứng với mỗi hang(n =1 , n=2 , n =3 , n=4)thì mỗi cột nó sẽ có các số được in ra khác nhau



