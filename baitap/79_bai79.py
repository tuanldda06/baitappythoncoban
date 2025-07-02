#Viết hàm với tham số truyền vào là một danh sách các số thực. Kiểm tra xem danh sách có phải là danh sách giảm không.
def xuly(danhsach) :
    for sothutu in range(len(danhsach)-1) :
        if danhsach[sothutu] < danhsach[sothutu + 1] :
            return False
    return True
danhsach = input().split()
if len(danhsach)== 0 :
    print('Danh sach rong')
else : 
    try : 
        danhsachso = list(map(float,danhsach))
        ketqua = xuly(danhsachso)
        print(ketqua)
    except :
        print('Dinh dang dau vao khong hop le')
