#Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng.
a =input('Nhap day so can tinh la:')
b = list(map(int, a.split()))
def tuan(danhsach):
    return sum(danhsach)
print('Tong la:',tuan(b))    