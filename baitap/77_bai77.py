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
