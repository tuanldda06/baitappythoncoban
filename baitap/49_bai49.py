#Viết hàm tính n giai thừa (n!). Với tham số là số tự nhiên n.
def giaithua(n):
    if n == 1 :
        return 1
    else :
        return n * giaithua(n-1)
try :
    n = int(input())
    if n < 0 :
        print('Vui long nhap so tu nhien')
    else :
        print(giaithua(n))
except :
    print('Dinh dang dau vao khong hop le')