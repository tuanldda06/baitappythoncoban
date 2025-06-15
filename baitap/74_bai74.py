#Viết hàm với tham số truyền vào là chuỗi s. Trả về list các ký tự theo thứ tự đảo ngược của chuỗi s.
def xuly(s) :
    chuoi =[]
    if len(s) == 0 :
        return chuoi
    for i in s[::-1] :#split() không cần thiết vì bạn chỉ cần lặp qua từng ký tự của chuỗi đảo ngược. Chuỗi trong Python có thể được lặp trực tiếp, và s[::-1] đã cung cấp thứ tự đảo ngược.
#Trong code gốc, bạn dùng else sau if len(s) == 0. Điều này đúng về mặt cú pháp nhưng không cần thiết, vì return chuoi trong if đã thoát hàm, nên khối mã tiếp theo chỉ chạy khi len(s) > 0.        
        chuoi.append(i)
    return chuoi
s = input()
print(xuly(s))