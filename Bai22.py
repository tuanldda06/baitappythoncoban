#Dùng hàm input() và hàm split() để nhận số đo ba cạnh a, b, c từ bàn phím.
#Ép kiểu dữ liệu của a, b, c sang số thực để xử lý cho chính xác vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Dùng cấu trúc rẽ nhánh if … else với điều kiện phù hợp để giải quyết yêu cầu của bải toán.
#Ba cạnh a, b, c của một tam giác phải thỏa mãn điều kiện là tổng hai cạnh bất kỳ luôn lớn hơn cạnh còn lại. Tức là a+b>c và a+c>b và b+c>a.
#Tam giác vuông là tam giác có bình phương một cạnh bằng tổng bình phương hai cạnh còn lại. Ta kiểm tra điều kiện: a*a==b*b+c*c hoặc b*b==a*a+c*c hoặc c*c== a*a+b*b
#Tam giác đều là tam giác có ba cạnh bằng nhau. Ta kiểm tra điều kiện a==b và b==c
#Tam giác cân là tam giác có hai cạnh bằng nhau. Ta kiểm tra điều kiện: a==b hoặc a==c hoặc b==c
#Tam giác tù là tam giác có một góc lớn hơn 90 độ. Từ điều kiện kiểm tra tam giác vuông, ta suy ra điều kiện để là tam giác tù là: a*a>b*b+c*c hoặc b*b>a*a+c*c hoặc c*c >a*a+b*b
#Trường hợp còn lại sẽ là tam giác nhọn.
a, b, c = map(float, input('Nhap lan luot do dai 3 canh : ').split())
if a + b > c and b + c > a and a + c > b:
    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        tamgiac = 'Tam giac vuong'
    elif a == b and b == c:
        tamgiac = 'Tam giac deu'
    elif a == b or a == c or b == c:
        tamgiac = 'Tam giac can'
    elif a * a > b * b + c * c or b * b > a * a + c * c or c * c > a * a + b * b:
        tamgiac = 'Tam giac tu'
    else:
        tamgiac = 'Tam giac nhon'
    print('{} {} {} la ba canh cua mot {}'.format(a, b, c, tamgiac))
else:
    print('{} {} {} khong phai la ba canh cua mot tam giac'.format(a, b, c))

  
  
    
