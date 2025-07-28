#Bài toán vector hóa , yêu cầu :
# Tạo hai mảng 1D kích thước 5 , chứa só ngẫu nhiên từ 1 đến 10
# Tính tổng tích và hiệu của hai mảng không dùng đến vòng lặp
import numpy as np
np.random.seed(42)
#đảm bảo kết quả được tái lập có nghĩa là mỗi lần bạn chạy mã với cùng giá trị seed() thì các số ngấu nhiên được taọ ra bởi hàm np.random.randiant() sẽ luôn giống nhau về giá trị và thứ tự
arr1 = np.random.randint(1,11, size = 5)
arr2 = np.random.randint
