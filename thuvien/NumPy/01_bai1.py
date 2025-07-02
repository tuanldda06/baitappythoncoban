#Bài 1: Tạo và thao tác mảng (Dễ)
#Yêu cầu:
#Tạo mảng 1D chứa 10 số từ 0 đến 9.
#Tạo mảng 2D 3x3 chứa các số từ 1 đến 9.
#Tính tổng, trung bình, và giá trị lớn nhất của mảng 2D.
import numpy as np
arr_1d= np.arange(10)
print('Mang 1D:' , arr_1d)
arr_2d = np.arange(1,10).reshape(3,3)
print('\nMang2D : \n',arr_2d)
total = np.sum(arr_2d)
mean = np.mean(arr_2d)
max_val = np.max(arr_2d)
print('\nTong:',total)
print('Trung binh',mean)
print('Gia tri lon nhat',max_val)

