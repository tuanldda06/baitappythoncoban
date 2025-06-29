#Viết hàm trả về từ có độ dài lớn nhất trong chuỗi s. Với tham số truyền vào là chuỗi s.
# Nếu có nhiều từ có độ dài bằng nhau thì trả về từ có thứ tự nhỏ hơn (sắp xếp theo bảng chữ cái).
def xuly(s) :
    tudainhat = ''
    danhsach = s.split()
    for tu in danhsach :
        if (len(tu) > len(tudainhat)) or ((len(tu)==len(tudainhat)) and (tu<tudainhat)):
            tudainhat = tu
    return tudainhat
s = input()
print(xuly(s))