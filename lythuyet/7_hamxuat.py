#Hàm print có cú pháp như sau :
#      print(*objects , sep ='',end='\n',file=sys.stdout ,flush = False)
#*OBJECTS( hiểu đơn giản mọi thứ ở trong python đều là object:chuỗi , số ,...)
#Nó giúp ta truyền được nhiều argument vào hàm print với số lượng bất kì mà không phải ép kiểu dữ liệu.
#VD:
print('Tuannn' ,'beoooo')
print('Tuann'+'beooooooo')
print('Tuann' ,111)
#SEP : giá trị mặc định của sep là những khoảng trắng , và các giá trị sẽ nối với nhau bằng các parameter sep.
print('Tuannnn' ,'neeeee') #sep mặc định là khoảng trắng 
print('Tuannn' , 'neeeeee' , 'neeeeeee' , sep='#$$$')#sep ở đây là #$$$
print('Tuannn' ,'beo','nee',sep='')#sep ở đây là nối liền nhau do không có khoảng trắng
print('Tuannn' ,'beo','nee',sep=' ')#đây là sep ở dạng mặc định.
#END: kết thúc bằng.
#end ='\n'(mặc định)--> xuống dòng sau mỗi lần print
#end =''-->in tất cả trên 1 dòng , không có khoảng cách
#end =' '-->thêm khoảng trắng thay vì xuống dòng
#end ='|'-->thêm dấu phân cách tùy chỉnh
print('Hellooo',end =' ')
print('World')

print('Hello',end = '\n')
print('Tuann', end = '')
print('Tuan' ,end = '|')

#FILE : mặc định , hàm print sẽ ghi nội dung vào file sys.stdout, do đó ta có thể dùng hàm print như phương thức write.
with open('tuan.txt','w') as f :
    print('tuan ne',file = f)# hoặc f.write('tuan ne')
with open ('tuan.txt','r')  as f :
    print(f.read())

# Cuối cùng là FLUSH
#Khi flush = False(mặc định)-->có thể lưu dữ liệu vào bộ đệm trước khi hiển thị
#Khi flush = True-->In dữ liệu ngay lập tức , không giữ trong bộ nhớ đệm

