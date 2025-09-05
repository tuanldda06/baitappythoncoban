import math  
import numpy as np  # Dùng cho sin và cos

def grad(x):  # Định nghĩa hàm grad để tính đạo hàm của hàm f(x) = x^2 + 5*sin(x)
    return 2*x + 5*np.cos(x)  # Trả về giá trị đạo hàm f'(x) = 2x + 5cos(x)

def cost(x):  # Định nghĩa hàm cost để tính giá trị của hàm f(x) = x^2 + 5*sin(x)
    return x**2 + 5*np.sin(x)  # Trả về giá trị hàm số tại x

def myGD1(x0, eta):  # Định nghĩa hàm myGD1 thực hiện gradient descent, nhận điểm bắt đầu x0 và tốc độ học eta
    x = [x0]  # Khởi tạo danh sách x chứa điểm bắt đầu x0
    for it in range(100):  # Lặp tối đa 100 lần để cập nhật x
        x_new = x[-1] - eta * grad(x[-1])  # Tính giá trị mới của x theo công thức: x_new = x_cũ - eta * f'(x_cũ)
        if abs(grad(x_new)) < 1e-3:  # Kiểm tra điều kiện dừng: nếu |f'(x_new)| < 0.001 thì thoát vòng lặp
            break  # Thoát khỏi vòng lặp nếu điều kiện dừng được thỏa mãn
        x.append(x_new)  # Thêm giá trị x_new vào danh sách x
    return (x, it)  # Trả về danh sách các giá trị x và số vòng lặp đã thực hiện

# Thử nghiệm với các điểm bắt đầu khác nhau x0 = -5 và x0 = 5, tốc độ học eta = 0.1
(x1, it1) = myGD1(-5, 0.1)  # Chạy gradient descent với x0 = -5, eta = 0.1, lưu kết quả vào x1 (danh sách) và it1 (số vòng lặp)
(x2, it2) = myGD1(5, 0.1)  # Chạy gradient descent với x0 = 5, eta = 0.1, lưu kết quả vào x2 (danh sách) và it2 (số vòng lặp)


print("Nghiệm x1 = %f, giá trị hàm = %f, sau %d vòng lặp" % (x1[-1], cost(x1[-1]), it1))  # In giá trị cuối của x1, giá trị hàm tại x1[-1], và số vòng lặp
print("Nghiệm x2 = %f, giá trị hàm = %f, sau %d vòng lặp" % (x2[-1], cost(x2[-1]), it2))  # In giá trị cuối của x2, giá trị hàm tại x2[-1], và số vòng lặp
