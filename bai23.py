#Nhập file input và xác định loại tam giác
#Dữ liệu đầu vào lưu trữ trong file "Bai2.9.inp"
#Ba cạnh a, b, c của một tam giác phải thỏa mãn điều kiện là tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại. Tức là a+b>c và a+c>b và b+c>a.
#Tam giác vuông là tam giác có bình phương một cạnh bằng tổng bình phương hai cạnh còn lại. Ta kiểm tra điều kiện: a*a==b*b+c*c hoặc b*b==a*a+c*c hoặc c*c== a*a+b*b
#Tam giác đều là tam giác có ba cạnh bằng nhau. Ta kiểm tra điều kiện a==b và b==c
#Tam giác cân là tam giác có hai cạnh bằng nhau. Ta kiểm tra điều kiện: a==b hoặc a==c hoặc b==c
#Tam giác tù là tam giác có một góc lớn hơn 90 độ. Từ điều kiện kiểm tra tam giác vuông, ta suy ra điều kiện để là tam giác tù là: a*a>b*b+c*c hoặc b*b>a*a+c*c hoặc c*c >a*a+b*b
#Trường hợp còn lại sẽ là tam giác nhọn.
#Lỗi sẽ phát sinh ở lệnh open() nếu file input không tồn tại. Dùng lệnh except bắt lỗi FileNotFoundError và xử lý.
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi và xử lý.
#Sử dụng câu lệnh with với hàm open() và mode='w' nhằm mở file để ghi thông báo lỗi
filename = "Bai2.9.inp"
content = input('Nhap lan luot ba canh la :')
with open(filename , 'w') as file :
  file.write(content)
try :
  with open("Bai2.9.inp" , 'r') as fileInp:
    danhsach = fileInp.read()
    a , b , c = map(float ,danhsach.split())
  if a+b>c and a+c>b and b+c>a :
    if a*a == b*b + c*c or b*b = a*a + c*c or c*c = a*a + b*b :
       tamgiac = 'Vuong'
    elif a == b and c ==b :
       tamgiac = 'Deu'
    elif a==c or b==c or a==b:
       tamgiac = 'Can'
    elif a*a >b*b+c*c or b*b>a*a + c*c or c*c>a*a+b*b:
       tamgiac = 'Tu'
    else :
       tamgiac = 'Nhon'
      thongbao='{} {} {} la ba canh cua mot tam giac{}'.format(a,b,c,tamgiac))
  else :
      thongbao='{} {} {} khong phai la ba canh cua mot tam giac{}'.format(a,b,c))
except FileNotFoundError :#bắt lỗinếu file input không tồn tại
   thongbao ='File input khong ton tai'
except ValuaError : # Bắt lỗi nếu dữ liệu nhập vào không phải số
   thongbao ='Dinh dang dau vao khong hop le'
except Exception as e :# bắt mọi lỗi
   thongbao ='Loi'
with open('Bai2.9.out','w') as fileOut :
  fileOut.write(thongbao)
  print(thongbao)
 

      
    
  
