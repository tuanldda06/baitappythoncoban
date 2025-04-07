#Nhập & tính tổng dãy số nguyên bất kỳ cách nhau bởi khoảng trắng.
a = input('Nhap day so can tinh la:')   
b = list(map(int,a.split()))
tongdayso = sum(b)
print(b)