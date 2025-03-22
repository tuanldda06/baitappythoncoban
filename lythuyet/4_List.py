# Một List được giới hạn bởi cặp ngoặc '[]' ,tất cả những phần tử trong này đều là phần từ của List.
#Các phần tử cách nhau bởi dấu phẩy.
#Chứa mọi giá trị , mọi đối tượng của python và bao gồm chính nó
#VD : [3,'tuan',[4,'tuannnn]]
a = [3 ,'tuannn']
b =[44 ,'feeeee' , 444444]
c =[3]
print(a+b)
print(a*3)
print(c in b )#-->False
print(c in a )#--> True
#Indexing and cắt List
a = [1 ,3,'beooo',44,['tuannn',4]]
print(a[-1])
print(a[2:4])
#Thay đổi nội dung List
a = ['tuan','beooo',444,55,'neeeeeee']
a[3]=40
print(a)
#Ma trận : Là 1 list chứa một list khác
a = [[1,2,3],[4,5,6]]
print(a)
#Toán tử is : xem 1 biến A và B có trỏ về cùng 1 giá trị hay không
a = [1,2,3]
b = [1,2,3]
print(a is b ) #--> False , mặc dù cùng giá trị nhưng nó là 2 đối tượng khác nhau trong python.
# nó chỉ trả kết quả là True khi mà :
a = [1,2,3]
a=b
print(a is b ) #-->True
a[1] = 100
print(a)
print(b)


