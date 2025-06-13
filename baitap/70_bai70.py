#Viết hàm với tham số truyền vào là chuỗi s. Trả về tổng và trung bình cộng của các từ là số tự nhiên trong chuỗi s.
def xuly(s):
    tong = 0
    dem = 0
    for c in s :
        if c.isdigit() :
            dem +=1
            tong +=int(c)
        if dem == 0 :
            return 0 , 0
        tb = tong / dem
        return tong , tb
s = input()
tong,trungbinh = xuly(s)
print(tong)
print(trungbinh)