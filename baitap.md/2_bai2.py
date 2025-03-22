#Tính tổng hai số nguyên bất kỳ (Có xử lý ngoại lệ đầu vào).

# try: Chứa đoạn code có thể gây lỗi.
# except: Bắt lỗi và xử lý.
# except Exception as e: Bắt mọi lỗi và lưu chi tiết lỗi vào e.
# else: Chạy khi không có lỗi.
# finally: Luôn chạy dù có lỗi hay không.
try :
    print('Nhap so thu nhat:')
    so1= int(input())
    print('Nhap so thu hai:')
    so2=int(input())
    print('Tong cua hai so la:' , str(so1+so2))
except :
    print('Dinh dang sai du lieu!')
except Exception as e :
    print('Tuannnnn')
else :
    print('Hiii neeee')
finally :
    print('Tuạnnnn')
    