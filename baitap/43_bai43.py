#Viết hàm trả về tên của bạn có chiều cao lớn hơn (Tham số là tên và chiều cao)
#Định dạng đầu vào
#Gồm hai dòng:
#Dòng đầu tiên chứa tên và tuổi của bạn thứ nhất. Cách nhau bởi khoảng trắng
#Dòng thứ hai chứa tên và tuổi của bạn thứ hai. Cách nhau bởi khoảng trắng
#Định nghĩa hàm ten_ban_cao_hon với các tham số là tên và chiều cao của hai bạn
#Sử dụng cấu trúc rẽ nhánh để so sánh chiều cao của hai bạn
#Dùng hàm return để trả về tên của bạn cao hơn
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() và hàm split() để nhập các giá trị từ bàn phím.
#Chuyển giá trị chiều cao mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp chiều cao nhỏ hơn 1 và chiều cao bằng nhau. Hiển thị thông báo nếu có.
#Gọi hàm ten_ban_cao_hon và truyền vào tham số tên, chiều cao của hai bạn
#Hiển thị ra màn hình kết quả theo định dạng đầu ra yêu cầu
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
def ten_ban_cao_hon(ten1 , ten2 ,chieucao1 , chieucao2):
  if chieucao1 > chieucao2 :
    return ten1
  else :
    return ten2
try :
  ten1 , chieucao1 = input().split()
  ten2 , chieucao2 = input().split()
  chieucao1 = int(chieucao1)
  chieucao2 = int(chieucao2)
  if chieucao1 < 1 or chieucao2 < 1 :
    print('Loi khong xay ra')
  elif chieucao1 == chieucao2 :
    print('{} cao bang{}'.format(ten1,ten2))
  else :
    ketqua=ten_ban_cao_hon(ten1,ten2 ,chieucao1 ,chieucao2)
    print('{} cao hon'.format(ketqua))
except :
  print('Dinh dang dau vao khong hop le')