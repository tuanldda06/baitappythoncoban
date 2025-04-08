#Xuất file output trên 1 dòng từ chuỗi input bất kỳ nhập vào từ nhiều dòng ( xử lý ngoại lệ đầu vào)
#Input :Dữ liệu đầu vào lưu trữ trong file "Bai1.12.inp" ,gồm n dòng với n là độ dài của câu chào ,mỗi dòng chứa một từ của câu
#Output :Dữ liệu đầu ra lưu trữ trong file "Bai1.12.out" ,gồm một dòng duy nhất hiển thị câu chào, các từ cách nhau 1 khoảng trắng
#Lưu ý: Nếu file input không tồn tại thì xuất thông báo: Khong tim thay file input!
try :
    with open ('Bai1.12.inp','r') as fileInp :
        toanbofile = fileInp.read()
        danhsach = toanbofile.split()
        filehoanchinh = ' '.join(danhsach)
    with open ('Bai1.12.out','w') as fileOut :
        fileOut.write(filehoanchinh)
    with open ('Bai1.12.out','r') as fileOut :
        print(fileOut.read())
except FileNotFoundError:
    print('Khong tim thay file input!')