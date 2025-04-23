#Hiển thị ra màn hình các số nguyên tố trong đoạn từ a đến b. (Với a <= b, a,b là số nguyên tố)
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập hai giá trị a, b từ bàn phím.
#Chuyển hai giá trị mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp a, b nhỏ hơn 0 và a > b. Hiển thị thông báo lỗi nếu có.
#Sử dụng vòng lặp for để duyệt các số từ a đến b
#Với mỗi số được duyệt qua, kiểm tra số đó có phải là số nguyên tố không (Tham khảo Bài 3.16)
#Nếu là số nguyên tố thì dùng hàm print() kết hợp với tham số end để hiển thị kết quả theo định dạng đầu ra yêu cầu
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
import math
try :
    a = int(input())
    b = int(input())
    if a< 0 or b < 0 :
        print('Phai la so tu nhien')
    elif a > b :
        print( 'a phai be hon b')
    else :
        for i in range(a,b+1):
            if i >1 :
                for j in range (2,int(math.sqrt(i))+1) :
                    if i % j == 0 :
                        print('Day la so nguyen to')
                        break
                else :#đây là else của vòng lặp for, không phải của câu lệnh if.
                    print(i , end = ' ')
except:
   print("Dinh dang dau vao khong hop le!")