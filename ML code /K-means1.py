import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import random
np.random.seed(18)#Đặt seed ngẫu nhiên để đảm bảo các phép toán ngẫu nhiên (như np.random.choice và np.random.multivariate_normal) cho kết quả giống nhau mỗi lần chạy.
means = [[2,2] , [8,3] ,[3,6]]# kỳ vọng của bài toán
cov = [[1,0] , [0,1]] #là ma trận đơn vị [[1, 0], [0, 1]], nghĩa là mỗi cụm có dạng hình cầu với phương sai 1 và không có tương quan giữa các chiều.
N = 500
X0=np.random.multivariate_normal(means[0] , cov , N) # ứng với kỳ vọng means[0] = [2,2]
X1=np.random.multivariate_normal(means[1] , cov , N) # ứng với kỳ vọng means[1] = [8,3]
X2=np.random.multivariate_normal(means[2] , cov , N) # ứng với kỳ vọng means[2] = [3,6]
X = np.concatenate((X0 , X1,X2) , axis = 0) # ghép nhiều mảng Numpy thành mảng lớn hơn , axis =   ghép nhiều hàng nối theo chiều dọc
K = 3 # 3 cụm
original_label = np.asarray([0]*N + [1]*N + [2]*N).T#Hàm np.asarray chuyển danh sách python thành 1 mảng numpy và tạo mảng kích thước (1500,) với 500 số 0 (cho X0), 500 số 1 (cho X1), và 500 số 2 (cho X2)


def kmeans_init_centroids(X , k ) :#Chọn ngẫu nhiên k hàng từ X làm tâm cụm ban đầu.
  return X[np.random.choice(X.shape[0] , k ,replace = False)] #Dùng np.random.choice với replace=False để đảm bảo không chọn trùng điểm.

def kmeans_assign_labels( X, centroids) :# tìm nhãn mới cho các điểm khi biết các tâm cụm
  D = cdist(x , centroids) 
  return np.argmin(D , axis = 1) #tìm chỉ số của tâm cụm gần nhất cho mỗi điểm, trả về mảng 1 chiều kích thước (N,) (ở đây là (1500,)).

def has_converged(centroids , new_centroids ) : # kiểm tra điều kiện dừng của thuật toán
  return (set[tuple(a) for a in centroids] == set([tuple(a) for a in new_centroids]))

def kmeans_update_centroids(X , labels , K ) :
  centroids = np.zeros((K , X , shape[1]))
  for k in range(K) :
    Xk = X[labels == k ,:] # thu thập tất cả các điểm được gán cho cụm K
    centroids[k ,:] = np.mean(Xk , axis = 0) # lấy trung bình
  return centroids













