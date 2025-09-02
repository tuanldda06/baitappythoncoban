import numpy as np
import matplotlib.pyplot as plt

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T  # Tạo mảng chiều cao (cm) với 13 giá trị, chuyển vị thành mảng 2D có hình dạng (13, 1).
y = np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])  # Tạo mảng cân nặng (kg) với 13 giá trị, hình dạng (13,)
plt.scatter(X, y, color="green")
plt.xlabel("Chieu cao(cm)")
plt.ylabel("Can nang(kg)")
plt.title("Chieu cao va can nang")
plt.grid(True)# Tắt lưới theo yêu cầu trước 
plt.show()

