#Viết hàm với tham số truyền vào là danh sách bất kỳ. Hiển thị các phần tử ra màn hình kèm với số thứ tự phía trước.
#Cách 1 :
def xuly(danhsach) :
    for i in range(len(danhsach)) :
        print('{}. {}'.format(i+1,danhsach[i]))
        #hoặc print(f"{i+1}. {danh_sach[i]}")
     # do cái này bắt đầu từ 1 nên i phải + thêm 1 vào , do chạy từ range nên sẽ bắt đầu từ 0 luôn
danhsach = input()
xuly(danhsach)
#Cách 2 :
def xuly(danhsach) :
    for thutu , giatri in enumerate(danhsach , start =1) :## Sử dụng enumerate với start=1 để số thứ tự bắt đầu từ 1 , do bth thì nó sẽ bắt đầu từ 0
        print(f'{thutu}. {giatri}')
danhsach = input()
xuly(danhsach)
#Cú pháp:  enumerate(iterable, start=0)
#iterable: Một đối tượng có thể lặp (như danh sách, chuỗi, tuple).
#start: Giá trị bắt đầu của số thứ tự (mặc định là 0).
#-->Trả về một iterator chứa các cặp (index, value).


