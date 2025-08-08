#Viết hàm với tham số truyền vào là một danh sách và số tự nhiên n. Trả về danh sách n phần tử bằng cách lặp lại danh sách được truyền vào.
#VD: danhsach :'Kteam Kteam 2021 Chuc Mung Nam Moi ' và n = 3 --> Output :Kteam Kteam 2021
def xuly(dsach , n):
    phandunguyen =(n // len(dsach) ) +1
    dsachlucdo = dsach * phandunguyen
    dsachcuoicung = dsachlucdo[:n]
    return dsachcuoicung
dsach = input().split()
if len(dsach) ==0 :
    print('Danh sach rong')
else :
    try :
      n = int(input())
      ketqua = xuly(dsach , n)
      print(*ketqua)
    except :
        print('Vui long cac so nguyen duong')
