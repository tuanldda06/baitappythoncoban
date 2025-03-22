#Định dạng bằng toán tử %
a = 'Hello Tuan %s'%('tuann')
print(a)
b = '%d'%(6.8)
print(b)
d = '%d'%(10/3)
print(d)# lấy phần nguyên
c = '%o'%(25)
print(c)# số thập phân trong hệ bát phân

# Định dạng bằng chuỗi f
a = 'tuann'
print(f'This is {a}')
b = 1000
print(f'this is {b}')
c = 'aa'
print(f'this is {{a}} {{b}} {c}')

#Định dạng bằng phương thức format
k = 'a:{0} b:{2} c:{1}'.format('22','tuan' ,'beo')
print(k)
k = 'a:{0} b:{2} c:{1}'.format('22','11111','tuan' ,'beo')
print(k)
a = '{:*^9}'.format('aaaaa')
print(a)# căn lề giữa với format
b = '{:$<11}'.format('aaaaaaaa')
print(b)# căn lề phải với format
c = '{:@>15}'.format('aaaaaaa')
print(c)# căn lề trái với format