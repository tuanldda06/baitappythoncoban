#Viết hàm liệt kê các số nguyên tố trong đoạn từ a đến b (Có gọi hàm kiểm tra số nguyên tố). Với tham số là hai số tự nhiên a và b (a <= b).
import math
def lietke(a,b) :
    for n in range(a,b+1):
        if n > 1 :
            for i in range(2,int(math.sqrt(n))+1) :#Nếu i có ước số nào (không phải 1 hoặc chính nó), thì ít nhất một ước số phải nhỏ hơn hoặc bằng √i.
                if n % i == 0 :
                    break #nếu mà i % j == 0  thì nó sẽ break và không chạy else còn nếu không t/m i % j == 0 thì nó sẽ thực hiện câu lệnh else
            # ở đây nếu kh dùng break thì nó xét hết tất cả các giá trị i
            # bài này chỉ yêu cầu liệt kê các giá trị nguyên tố , nên dùng break là hợp lý
            else :# else này là của for
                print(n , end = ' ') 
a = int(input())
b = int(input())
if a < 0 or b < 0 :
    print('Vui long nhap so tu nhien')
elif a > b :
    print('a phai be hon b')
else :
    lietke(a,b)
          