import numpy as np
import matplotlib.pyplot as plt
X = np.array([[147 , 150 , 153 , 158 , 163, 165 , 168 , 170 , 173,175,178 , 180 , 183]]).T# height(cm)
y = np.array([49 , 50 , 51,54,58,59,60 , 62,63,64,66,67,68]) #weight(kg)
one = np.ones((X.shape[0] ,1))#Tạo mảng cột chứa toàn số 1, có hình dạng (13, 1), đại diện cho hệ số chặn (intercept) trong hồi quy tuyến tính
Xbar = np.concatenate((one , X) , axis =1) # mỗi hàng là 1 điểm dữ liệu
A = np.dot(Xbar.T , Xbar)
b = np.dot(Xbar.T , y)
w = np.dot(np.linalg.pinv(A) , b)
# trọng số 
w_0 , w_1 = w[0] , w[1]
print(f"Hệ số chặn (w_0): {w_0:.2f}")
print(f"Hệ số góc (w_1): {w_1:.2f}")
# Vẽ biểu đồ phân tán và đường hồi quy
plt.scatter(X, y, color='blue', label='Dữ liệu')
x_line = np.array([[X.min()], [X.max()]])  # Điểm đầu và cuối để vẽ đường hồi quy
y_line = w_0 + w_1 * x_line  # Tính giá trị y dự đoán
plt.plot(x_line, y_line, color='red', label='Đường hồi quy')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.title('Hồi quy tuyến tính: Chiều cao vs Cân nặng')
plt.grid(False)  # Tắt lưới theo yêu cầu trước
plt.legend()#Sử dụng để hiển thị chú thích (legend) trên biểu đồ. Chú thích này giải thích ý nghĩa của các thành phần trong biểu đồ (như các đường, điểm, hoặc vùng) bằng cách hiển thị nhãn (label) tương ứng với chúng
plt.show()
