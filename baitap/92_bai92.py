#Viết hàm với tham số truyền vào là một danh sách hai chiều kích thước MxN. Trả về danh sách phần tử có độ dài lớn nhất của mỗi hàng.
def nhap_dsach(M , N ) :
  dsach2chieu = []
  for _ in range(M) :
    hang = input().split()
    if len(hang)!= N :
      print('Khong co cung kich thuoc')
      return None
    dsach2chieu.append(hang)
  return dsach2chieu
def phan_tu_dainhat(danhsach) :
  if not danhsach :
    return " "
  dodaichuoi = [len(ptu) for ptu in danhsach]
  dodaimax = max(dodaichuoi)
  vitridainhat = danhsach.index(dodaimax)
  return danhsach[vitridainhat]
def xuly(dsach2chieu):
  if not dsach2chieu :
    return " "
  ketqua = []
  for hang in dsach2chieu :
    phantudainhat = phan_tu_dainhat(hang)
    ketqua.append(phantudainhat)
  return ketqua
M = int(input())
N = int(input())
if M <= 0 or N <= 0 :
  print('Nhap kich thuoc la so nguyen duong')
  exit()

dsach2chieu = nhap_dsach(M , N)
if dsach2chieu is None :
  exit()

ketqua = xuly(dsach2chieu)
print(ketqua)
