#Viết hàm trả về chuỗi s sau khi xóa các khoảng trắng thừa.
def xuly(s):
    return ' '.join(s.split())
s = input()
print(xuly(s))