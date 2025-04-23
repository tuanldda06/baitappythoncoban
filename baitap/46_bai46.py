#Viết hàm máy tính đơn giản cho hai số thực (Chứa 4 hàm con +, -, x, %)
#Định dạng đầu vào
#Gồm một dòng duy nhất chưa ba giá trị {số thứ nhất} {phép tính}
#{số thứ hai} trên 1 dòng, cách nhau bởi khoảng trắng.
#Với:
#{số thứ nhất} và {số thứ hai} là hai số thực
#{phép tính} là một trong các dấu ['+', '-', 'x', ':']
#Định dạng đầu ra
#Gồm một dòng duy nhất hiển thị như sau: 
#Nếu là phép tính chia và {số thứ hai} bằng 0: So chia phai khac 0!
#Nếu biểu thức hợp lệ: {so thu nhat} {phep tinh} {so thu hai} = {ket qua}
#Định nghĩa hàm cong, tru, nhan, chia với tham số là hai số cần tính toán
#Đối với hàm chia, sử dụng cấu trúc rẽ nhánh để xử lý trường hợp số chia bằng 0
#Định nghĩa hàm may_tinh với tham số là hai số cần tính và phép tính:
#Sử dụng cấu trúc rẽ nhánh để gọi các hàm tương ứng với phép tính và trả về kết quả
#Sử dụng cấu trúc Xử lý ngoại lệ để xử lý các trường hợp gây ra lỗi
#Đặt toàn bộ chương trình trong khối try.
#Dùng hàm input() và hàm split() để nhận ba giá trị {số thứ nhất}, {phép tính} và {số thứ hai} từ bàn phím.
#Ép kiểu dữ liệu của {số thứ nhất} và {số thứ hai} sang số thực để xử lý vì các giá trị nhận được từ hàm input() mặc định sẽ ở kiểu chuỗi.
#Gọi hàm may_tinh và truyền vào các tham số cần thiết
#Nếu hàm trả về lỗi chia cho 0 thì xuất thông báo lỗi, còn không thì hiển thị kết quả ra màn hình theo định dạng đầu ra yêu cầu.
#Lỗi sẽ phát sinh ở lệnh ép kiểu nếu định dạng đầu vào không hợp lệ. Dùng lệnh except để bắt lỗi:
#Dùng hàm print() hiển thị thông báo lỗi ra màn hình

