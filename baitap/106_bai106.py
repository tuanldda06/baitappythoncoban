#Viết hàm với tham số truyền vào là một set gồm các số thực. Trả về giá trị lớn nhất, giá trị nhỏ nhất và tổng các phần tử của set.
def xuly(setX) :
  return max(setx) , min(setX) , sum(setX)
danhsach = input().split()
if len(danhsach) == 0 :
  print('Danh sach rong ')
else :
  try :
    setX = set(map(float , danhsach))
    thong_tin_set = xuly(setX)
    print(*thong_tin_set , sep = '\n\)
  except ValueError :
    print('Vui long nhap du lieu la so thuc')
