#Viết hàm liệt kê các số hoàn thiện nhỏ hơn n (Có gọi hàm kiểm tra số hoàn thiện). Với tham số tự nhiên n.
#Số hoàn thiện là số nguyên dương mà tổng các ước số thực sự (các ước nhỏ hơn chính nó) bằng chính số đó.
#Ví dụ:
#Số 6 có các ước thực sự là 1, 2, 3. Tổng: 1 + 2 + 3 = 6 → 6 là số hoàn thiện.
#Số 28 có các ước thực sự là 1, 2, 4, 7, 14. Tổng: 1 + 2 + 4 + 7 + 14 = 28 → 28 là số hoàn thiện.
#Số 8 có các ước thực sự là 1, 2, 4. Tổng: 1 + 2 + 4 = 7 ≠ 8 → 8 không phải số hoàn thiện.
def xuly(n) :
    if n <=1 :
        return False #Nếu n <= 1, trả về False (đúng, vì số hoàn thiện phải là số nguyên dương lớn hơn 1).
    else :
        tong = 0 
        for i in range(1,n) :#Số hoàn thiện là số nguyên dương mà tổng các ước số thực sự (các ước nhỏ hơn chính nó) bằng chính số đó.
            if n % i == 0 :
                tong +=i
        return tong == n #Tính tổng các ước thực sự (từ 1 đến n-1) và kiểm tra xem tổng này có bằng n hay không.
def kiemtraso(n) :
    for a in range(1,n) :
        if xuly(a) :
            print(a, end = ' ')
n = input()
kiemtraso(n) # do đề bài yêu cầu liệt kê các số hoàn thiện
#Cú pháp return tong == n:
#tong == n là một biểu thức so sánh, trả về giá trị boolean (True hoặc False).
#Nếu tong bằng n, biểu thức trả về True.
#Nếu tong khác n, biểu thức trả về False.
#Từ khóa return trả giá trị này về cho nơi gọi hàm (trong trường hợp này là hàm kiemtraso(n)).
