#Viết hàm nối các từ của chuỗi s bằng dấu "-"
def xuly(s):
    return '-'.join(s.split())#→ tách chuỗi s thành danh sách các từ (tự động bỏ khoảng trắng thừa).
s = input()
print(xuly(s))