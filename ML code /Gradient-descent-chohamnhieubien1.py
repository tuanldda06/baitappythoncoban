import numpy as np  # Nhập thư viện NumPy,
from sklearn.linear_model import LinearRegression  # Nhập lớp LinearRegression từ thư viện scikit-learn, dùng để thực hiện hồi quy tuyến tính.
X = np.random.rand(1000, 1)  # Tạo mảng 1000x1 chứa các số ngẫu nhiên từ 0 đến 1, đại diện cho biến độc lập (đặc trưng đầu vào) của hồi quy.
y = 4 + 3 * X + .5 * np.random.randn(1000, 1)  # Tạo biến phụ thuộc (mục tiêu) theo công thức y = 4 + 3X + nhiễu, trong đó nhiễu được phân phối chuẩn với trung bình 0 và độ lệch chuẩn 0.5.
model = LinearRegression()  # Khởi tạo một đối tượng mô hình LinearRegression từ scikit-learn để thực hiện hồi quy tuyến tính.
model.fit(X.reshape(-1, 1), y.reshape(-1, 1))  # Huấn luyện mô hình trên dữ liệu đầu vào X và mục tiêu y, định dạng lại X và y để đảm bảo chúng là mảng 2D như yêu cầu của scikit-learn (chuyển từ (1000,) thành (1000, 1)).
w, b = model.coef_[0][0], model.intercept_[0]  # Trích xuất độ dốc (trọng số, w) và hệ số chặn (bias, b) từ mô hình đã huấn luyện; model.coef_ là hệ số (độ dốc), model.intercept_ là hệ số chặn trên trục y.
sol_sklearn = np.array([b, w])  # Tạo một mảng NumPy chứa hệ số chặn (b) và độ dốc (w) làm kết quả của mô hình hồi quy tuyến tính.
print("Solution found by sklearn:", sol_sklearn)  # In ra kết quả (hệ số chặn và độ dốc) thu được từ mô hình đã huấn luyện.
