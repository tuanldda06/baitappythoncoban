#Viết hàm với tham số truyền vào là chuỗi s. Trả về số lượng từ vừa chứa ký tự, vừa chứa chữ số trong chuỗi s.
#Cách 1
def xuly(s):
    dem = 0 
    for tu in s.split() :# nếu không có split() thì nó sẽ duyệt cả khoảng trắng, ở đây yêu cầu xét từng kí tự
       cochu = False
       coso = False
       for c in tu :
           if c.isdigit() :
               coso = True
           if c.isalpha() :
               cochu = True
       if coso and cochu :
           dem +=1
    return dem    
s = input()
print(xuly(s))
#Cách 2
def xuly(s) :
    dem = 0
    for tu in s.split() :# nếu không có split() thì nó sẽ duyệt cả khoảng trắng, ở đây yêu cầu xét từng kí tự
       coso = 0
       cochu = 0
       for c in tu :
           if c.isdigit() :
               coso +=1
           if c.isalpha() :
               cochu +=1
       if coso >=1 and cochu>=1 :
           dem +=1
    return dem
s = input()
print(xuly(s))
           

