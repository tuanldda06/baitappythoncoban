#Viết hàm trả về hai danh sách sau khi đã hoán đổi nữa sau danh sách cho nhau. (Tham số là 2 danh sách bất kỳ).
#Định dạng đầu vào :Gồm hai dòng:
#Dòng đầu tiên chứa các phần tử của danh sách 1, các phần tử cách nhau bởi khoảng trắng
#Dòng thứ hai chứa các phần tử của danh sách 2, các phần tử cách nhau bởi khoảng trắng
#Định dạng đầu ra :Gồm hai dòng chứa hai danh sách kết quả sau khi đã hoán đổi nửa sau danh sách cho nhau, các phần tử cách nhau bởi khoảng trắng.
#Lưu ý: Nếu danh sách có số lẻ phần tử thì lấy nửa danh sách nhiều hơn để hoán đổi.
def xuly(dsach1 , dsach2) :
  nuadodai1 = len(dsach1) //2 
  nuadodai2 = len(dsach2) //2
  nuasaudsach1 = dsach1[dodai1:] # chạy đến hết dãy luôn
  nuasaudsach2 = dsach2[dodai2:]
  dsach1 = dsach1[:nuadodai1] + nuasaudsach2 # chạy đến nuadodai1 -1 rồi cộng thêm
  dsach2 = dsach2[:nuadodai2] + nuasaudsach1
dSach1 = input().split()
dSach2 = input().split()

#Goi thuc thi ham va truyen tham so cho ham
dsHoanDoi1, dsHoanDoi2 = hoan_doi_danh_sach(dSach1, dSach2)
#Unpacking arguments
print(*dsHoanDoi1)
print(*dsHoanDoi2)
  
