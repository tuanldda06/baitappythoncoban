#Viết hàm xóa các ký tự trùng lặp trong chuỗi. (Tham số truyền vào là chuỗi s).
def xuly(s):
    chuoi=""
    for i in s :
        if i not in chuoi :# nếu ký tự chưa từng xuất hiện → thêm vào.
            chuoi +=i
    return chuoi
s = input()
print(xuly(s))