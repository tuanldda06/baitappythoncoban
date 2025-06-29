#Viết hàm với tham số truyền vào là một danh sách các số thực. Trả về phần tử có giá trị nhỏ nhất (Không dùng hàm min).
def xuly(danhsach):
    sonhonhat = danhsach[0]
    for so in danhsach :
        if so < sonhonhat :
            sonhonhat = so
danhsach = input().split()
if len(danhsach) == 0 :
    print('Danh sach rong')
else :
    try :# Câu lệnh có thể gây lỗi do danhsach có thể chứa các kí tự khác số thực
        danhsachso = list(map(float , danhsach))
        sonhonhatt = xuly(danhsachso)
        print(sonhonhatt)
    except:
        print('Vui long nhap so thuc')
#Mục đích của sonhonhat = danhsach[0] là nó sẽ gán phần tử đầu tiên của danhsach cho biến là sonhonhat
#Ở đây do so sánh ở dạng là số nguyên , ta cũng không thế gán cho sonhonhat = 0 được 
#Bởi vì nếu hàm chỉ chứa các số nguyên dương lớn hơn 0 , thì hàm sẽ trả về 0 , điều đó vô lý
#VD : hàm là 1 2 3 5 99 thì khi gán sonhonhat = 0 thì kq sẽ trả về 0 , tuy nhiên trong hàm số nhỏ nhất là 1 ( vô lý--> do đó phải gán)
