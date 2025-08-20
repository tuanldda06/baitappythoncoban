#Viết hàm với tham số truyền vào là một tuple các số thực. Viết hàm trả về tuple đã được sắp xếp theo thứ tự giảm dần.
def xuly(tupleX) :
  tuplekq = tuple(sorted(tupleX , reverse = True))
  #Trong Python, tuple là một kiểu dữ liệu bất biến (immutable), nghĩa là không thể thay đổi nội dung của nó sau khi được tạo. Do đó, tuple không có phương thức sort().
  return tuplekq
tupleX = tuple(input().split())
ktra_tuple = all(ptu.isdigit() for ptu in tupleX)
if ktra_tuple :
  ketqua = xuly(tupleX)
  print(ketqua)
else :
  print('Dinh dang dau vao khong hop le')
  
