#Viết hàm với tham số truyền vào là một tuple các phần tử chỉ bao gồm chữ số. Trả về số nguyên được tạo ra từ các phần tử theo thứ tự trong tuple đó.
def xuly(tupleX) :
  number = int(''.join(tupleX))
  return number
tupleX = tuple(input().split())
ktra_tuple = all(pTu.isdigit() for pTu in tupleX)
if ktra_tuple: 
  ketqua = xuly(tupleX)
  print(ketqua)
else :
  print('Dinh dang dau vao khong hop le')
