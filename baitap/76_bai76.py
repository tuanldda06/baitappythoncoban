#Viết hàm với tham số truyền vào là một danh sách các số thực. Trả về trung bình cộng của danh sách đó.
def trung_binh(danhsach) :
    tong = sum(danhsach)
    sophantu = len(danhsach)
    trungbinhcong = tong / sophantu
    return trungbinhcong
danhsach = input().split()
if len(danhsach) == 0:
    print('Danh sach rong')
else :
    danhsachso = list(map(float , danhsach))
    trungbinhcong = trung_binh(danhsachso)
    print(trungbinhcong)


        
