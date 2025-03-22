#Nhập số bất kỳ ở hệ thập phân và hiển thị ra ở hệ bát phân.(Có xử lý ngoại lệ đầu vào)
try: 
    Nhapsothapphan = int(input())
    print('So thap phan %d trong he bat phan la %o'%(Nhapsothapphan,Nhapsothapphan))
except:
    print('dinh dang dau vao khong hop le!')
#Khi bạn nhập dữ liệu bằng input(), giá trị nhận được luôn là chuỗi(str) .
# Vậy khi nhập 3.6 nó sẽ ghi lỗi vì khi đó sẽ là'3.6' , do chuỗi có dấu'.' nên sẽ không t/m
# Nhưng khi nhập là 4 thì nó sẽ là '4' ,t/m đk của đề   
# nên nếu muốn nhập 3.6 vào thì phải qua hàm float trước rồi mới int()
#VD: float('3.6')-->3.6-->int(3.6)-->3(lấy phần nguyên kh làm tròn)
