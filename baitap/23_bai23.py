#Viết chương trình nhập vào từ file input ba số a, b, c. Nếu a, b, c là ba cạnh của một tam giác thì kiểm tra và xuất ra file output thông báo loại của tam giác (Có xử lý ngoại lệ đầu vào).
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Sử dụng câu lệnh with với hàm open() và mode='r' nhằm mở file để đọc.
#Dùng hàm readline() để đọc dữ liệu dòng đầu tiên từ file input và lưu vào biến
#Sử dụng phương thức rstrip() để loại bỏ ký tự '\n' ở bên phải vì giá trị nhận được khi sử dụng hàm readline() bao gồm cả ký tự xuống dòng.
#Dùng hàm map(), float và hàm split() để nhận và ép kiểu dữ liệu của ba cạnh a, b, c sang số thực.
#Dùng cấu trúc rẽ nhánh if … else với điều kiện phù hợp để giải quyết yêu cầu của bải toán.
#Thuật toán:
#Ba cạnh a, b, c của một tam giác phải thỏa mãn điều kiện là tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại. Tức là a+b>c và a+c>b và b+c>a.
#Tam giác vuông là tam giác có bình phương một cạnh bằng tổng bình phương hai cạnh còn lại. Ta kiểm tra điều kiện: a*a==b*b+c*c hoặc b*b==a*a+c*c hoặc c*c== a*a+b*b
#Tam giác đều là tam giác có ba cạnh bằng nhau. Ta kiểm tra điều kiện a==b và b==c
#Tam giác cân là tam giác có hai cạnh bằng nhau. Ta kiểm tra điều kiện: a==b hoặc a==c hoặc b==c
#Tam giác tù là tam giác có một góc lớn hơn 90 độ. Từ điều kiện kiểm tra tam giác vuông, ta suy ra điều kiện để là tam giác tù là: a*a>b*b+c*c hoặc b*b>a*a+c*c hoặc c*c >a*a+b*b
#Trường hợp còn lại sẽ là tam giác nhọn.
#Lỗi sẽ phát sinh ở lệnh open() nếu file input không tồn tại. Dùng lệnh except bắt lỗi FileNotFoundError và xử lý.
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi và xử lý.
#Sử dụng câu lệnh with với hàm open() và mode='w' nhằm mở file để ghi thông báo lỗi
#giả sử lưu file input() chứa 3 số a b c là bai23.inp
try :
    with open('bai23.inp','r') as fileInp :
        s= fileInp.read()
        a,b,c = map(float ,s.split())
        if a + b>c and b+c>a and c+a >b :
            if a==b and c==a :
                loaitamgiac ='deu'
            elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a :
                loaitamgiac = 'vuong'
            elif a==b or b==c or a==c :
                loaitamgiac = 'can'
            elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > b*b + a*a :
                loaitamgiac ='tu'
            else :
                loaitamgiac = 'nhon'
            thongbao = '{} {} {} la ba canh cua tam giac {}'.format(a,b,c,loaitamgiac)
        else :
            thongbao = '{} {} {} khong phai la ba canh cua mot tam giac '.format(a,b,c)
except FileNotFoundError :
    thongbao = 'File khong ton tai'
except :
    thongbao = 'Dinh dang dau vao khong hop le'
with open ('bai23.out','w') as fileOut :
    fileOut.write(thongbao)
with open('bai23.out','r') as fileOut :
    print(fileOut.read())

