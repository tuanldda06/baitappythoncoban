#Viết hàm với tham số truyền vào là một tuple gồm các số thực. Trả về giá trị lớn nhất, giá trị nhỏ nhất, số phần tử của tuple.
def xuly(tupleX) :
  return max(tupleX) , min(tupleX) , len(tupleX)
danhsach = input().split()
if len(danhsach) == 0 :
  print('Danh sach rong')
else :
  try:
    tupleX = tuple(list(float , danhsach)))
    gtriMax , gtriMin , soPtu = xuly(tupleX)
    print(gtriMax)
    print(gtriMin)
    print(soPtu)
  except ValueError :
    print('Dinh dang dau vao khong hop le')
    
  
