#Viết chương trình hiển thị ra màn hình các số chia hết cho 5 (không quá 10 số) trong khoảng a, b. Với a, b là hai số nguyên nhập từ bàn phím (a <= b).
#Nếu quá 10 số thỏa điều kiện thì thông báo: In qua 10 so roi!
#Nếu đã in hết các số thỏa điều kiện thì thông báo: Da in het cac so chia het cho 5
#Lưu ý:
#Nếu a > b thì xuất thông báo: So thu nhat lon hon so thu hai!
#Nếu không có số nào chia hết cho 5 thì xuất thông báo: Khong co so nao chia het cho 5
#Nếu input nằm ngoài định dạng đầu vào thì xuất thông báo: Dinh dang dau vao khong hop le!##

#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập hai giá trị a, b từ bàn phím.
#Chuyển hai giá trị mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp a > b. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for với biến giá trị chạy từ a đến b: Kiểm tra điều kiện chia hết cho 5
#Nếu chia hết cho 5 thì tăng biến đếm.
#Kiểm tra xem biến đếm đã lớn hơn 10 chưa.
#Nếu đúng thì xuất thông báo và sử dụng break để thoát vòng lặp
#Nếu sai thì dùng hàm print() kết hợp với tham số end để xuất kết quả theo định dạng đề bài yêu cầu
#Sử dụng cấu trúc else của vòng for để xuất thông báo trường hợp không có số nào chia hết cho 5 và trường hợp đã in hết các số.
#Lưu ý: else của for được thực hiện khi vòng lặp thoát ra một cách bình thường, không gặp lệnh break hay lỗi.
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
    a = int(input())
    b = int(input())
    if a > b:
        print('a phai lon hon b')
    else :
        dem = 0
        for i in range (a , b+1):
            if i % 5 ==0 :
                dem +=1
                if dem > 10 :
                    print('In qua so roi')# dành cho i khi in quá 10 số chia hết cho 5
                    break
                print(i,end = ' ')
        else :
            if dem == 0 :
                print('Khong co so nao chia het cho 5')# dành cho i khi không có số nào chia hết cho 5
            else :
                print('Da in het so roi')# dành cho i khi vừa đủ hoặc ít hơn 10 số chia hết cho 5
except ValueError :
    print('Dinh dang dau vao khong hop le')


