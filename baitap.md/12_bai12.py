#Xuất file output trên 1 dòng từ chuỗi input bất kỳ nhập vào từ nhiều dòng
#Input :Dữ liệu đầu vào lưu trữ trong file "Bai1.12.inp" ,gồm n dòng với n là độ dài của câu chào ,mỗi dòng chứa một từ của câu
#Output :Dữ liệu đầu ra lưu trữ trong file "Bai1.12.out" ,gồm một dòng duy nhất hiển thị câu chào, các từ cách nhau 1 khoảng trắng

content = 'tuan\nbeo\nnee'# hoặc cũng có thể là content = input() nhưng phải đúng định dạng đề bài yêu cầu
with open ('bai1.10.inp','w') as file :
    file.write(content)
with open ('bai1.10.inp' , 'r') as fileInp:
    danhsach = fileInp.read()
    tachrachuoicon = danhsach.split()
    danhsachhoanchinh = ' '.join(tachrachuoicon)# nối các ký tự bằng khoảng trắng
with open ('bai1.10.out' ,'w') as fileOut:
    fileOut.write(danhsachhoanchinh)
with open('bai1.10.out','r') as fileOut :
    a= fileOut.read()
    print(a) 
#Phải code từ 5 đến 7 trước để lưu được dữ liệu vào file 'bai1.10.inp'