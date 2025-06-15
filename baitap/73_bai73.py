#Viết hàm với tham số truyền vào là số tự nhiên n. Trả về list số tự nhiên và list bình phương các số tự nhiên nhỏ hơn n.
def xuly(n):
    try :
        n = input()
    except ValueError :
        return [] , [] # Trả về hai danh sách rỗng nếu đầu vào không phải số nguyên
    if n < 1 :
        return [] ,[]
    else :
        sotunhien =[]
        binhphuong = []
        for i in range(n) :
            sotunhien.append(i)
            binhphuong.append(i*i)
        return sotunhien , binhphuong
n = int(input())
sotunhien , binhphuong = xuly(s)
print("Danh sách số tự nhiên:", sotunhien)
print("Danh sách bình phương:", binhphuong)
#phương thức append() là một phương thức của danh sách (list) được sử dụng để thêm một phần tử vào cuối danh sách.
#append() chỉ thêm một phần tử tại một thời điểm. Nếu muốn thêm nhiều phần tử, bạn cần gọi append() nhiều lần hoặc dùng extend()


            
        