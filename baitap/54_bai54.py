#Viết hàm truyền vào tham số là hai chuỗi s1 và s2. Trả về chuỗi kết quả bằng cách nối 2 chuỗi s1 và s2 sau khi được xử lý như sau: nếu độ dài chuỗi nào nhỏ hơn 5 thì lặp lại chuỗi đó 3 lần.
def xuly(s1,s2):
    if len(s1)<3 :
        s1 = s1*3
    if len(s2)<3 :
        s2 = s2*3
    return s1 + s2
s1 = input()
s2 = input()
print(xuly(s1,s2))