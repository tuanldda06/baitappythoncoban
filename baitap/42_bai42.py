#Hiển thị câu theo mẫu (Với tham số là {Ten} và {Tuoi} )
#Định nghĩa hàm xin_chao với hai tham số là tên và tuổi được truyền vào
#Dùng hàm print() để xuất thông báo theo yêu cầu đầu ra
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() để nhập hai giá trị tên và tuổi từ bàn phím.
#Chuyển giá trị tuổi mới nhận được sang kiểu số nguyên, vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Sử dụng cấu trúc rẽ nhánh để xử lý trường hợp tuổi nhỏ hơn 1. Hiển thị thông báo lỗi nếu có.
#Gọi hàm xin_chao và truyền vào tham số tên, tuổi
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình
try :
  ten = input()
  tuoi = int(input())
  if tuoi < 1 :
    print('Tuoi phai lon hon hoac bang 1')
  else :
    def xin_chao(ten , tuoi):
      return 'Xin chao!Toi ten la{} , toi {} tuoi'.format(ten,tuoi)
    print(xin_chao(ten,tuoi))
except :
  print('Khong hop le')