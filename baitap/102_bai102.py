#Viết hàm với tham số truyền vào là một tuple chứa các phần từ là tuple các số nguyên. Trả về tuple tổng của các tuple con, hiển thị tuple ban đầu và kết quả của hàm ra màn hình.
#Định dạng đầu vào : Dòng đầu tiên chứa số nguyên n không âm là số phần tử của tuple và n dòng tiếp theo, dòng thứ i chứa các phần tử của tuple con thứ i, các phần tử cách nhau bởi khoảng trắng.
#Định dạng đầu ra:Gồm hai dòng:Dòng đầu tiên hiển thị tuple người dùng nhập vào Và Dòng thứ hai hiển thị tuple tổng các tuple con.
def xuly(tuple) :
  tongtuple = tuple(sum(ptu) for ptu in tupleX))
  return tongtuple
try:
  n = int(input())
  listX = []
  for _ in range(n) :
    listptu = map(float , input().split())
    listX.append(listptu)
  tupleX = tuple(listX)
  print(tupleX)
  ketqua = xuly(tupleX)
  print(ketqua)
except :
  print('Dinh dang dau vao khong hop le')

  
