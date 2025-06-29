#Viết hàm với tham số truyền vào là một danh sách các số nguyên. Trả về danh sách các phần tử lẻ.
def xuly(danhsach) :
    danhsachsole = []
    for i in danhsach :
        if i % 2 != 0 :
            danhsachsole += i
    return danhsachsole
danhsach = input().split()
if len(danhsach) == 0 :
    print('Danh sach rong')
else :
    try :
        danhsachso = list(map(int , danhsach))
        dssole = xuly(danhsachso)
        print(*dssole)
    except :
        print('Vui long nhap dau vao la cac so thuc')

