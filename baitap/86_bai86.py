#Viết hàm với tham số truyền vào là hai danh sách cùng kích thước: danh sách tên và danh sách quốc tịch. 
#Hiển thị ra màn hình tên và quốc tịch tương ứng với vị trí trong danh sách.
def xoa_khoang_trang(s) :
  s=s.strip() #Phương thức strip() xóa tất cả khoảng trắng (hoặc ký tự trắng như tab, xuống dòng) ở đầu và cuối chuỗi.
  while '  ' in s :#Vòng lặp này kiểm tra xem chuỗi có chứa hai khoảng trắng liên tiếp hay không.
    s.replace('  ' ,' ')#Phương thức replace() thay thế mọi cặp hai khoảng trắng (" ") bằng một khoảng trắng (" ")
  return s
#Ngoài ra có thể dùng split() thay vì là strip()
#def xoa_khoang_trang(n) :
  #words = n.split() #Chia chuỗi s thành danh sách các từ, tự động loại bỏ tất cả khoảng trắng thừa (đầu, cuối, và giữa). Ví dụ: " John Doe " trở thành ["John", "Doe"].
  #n = ' '.join(words) #Nối các phần tử trong danh sách words thành một chuỗi, sử dụng một khoảng trắng (" ") làm ký tự phân tách. Ví dụ: ["John", "Doe"] trở thành "John Doe".
def noi_danh_sach(dsTen,dsQuoctich) :
  dsTen= [xoa_khoang_trang(ten) for ten in dsTen]
  dsQuoctich = [xoa_khoang_trang(quoctich) for quoctich in dsQuoctich]
  for ten,quoctich in zip(dsTen , dsQuoctich) :#hàm zip() trong Python sẽ ghép cặp các phần tử từ các danh sách đầu vào theo thứ tự tương ứng.
    print(ten + '-'+ quoctich) 
dsTen = input().split(',')
dsQuocTich = input().split(',')
#Kiem tra danh sach co cung kich thuoc hay khong
if len(dsTen) != len(dsQuocTich):
   print("Vui long nhap hai danh sach cung kich thuoc!")
else:   
   #Goi ham va truyen cac tham so can thiet
   in_danh_sach(dsTen, dsQuocTich)
  
  

