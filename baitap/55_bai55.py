#Viết hàm truyền vào tham số là hai chuỗi s1 và s2. Kiểm tra chuỗi s2 có xuất hiện trong chuỗi s1 không, nếu không thì hiển thị thông báo, nếu có thì hiển thị số lần xuất hiện.
def xuly(s1,s2):
    if s2 in s1 :
            #Su dung phuong thuc count() de dem so lan xuat hien cua chuoi con , cú pháp : chuoi.count(chuoi_con)   
        print(s1.count(s2))
    else :
        print('chuoi {} khong xuat hien trong {}'.format(s2,s1))
s1 = input()
s2 = input()
xuly(s1,s2)
