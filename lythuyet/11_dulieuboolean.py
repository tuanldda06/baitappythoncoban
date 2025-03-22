#Là một dữ liêu nhiều ngôn ngữ lập trình , chỉ có 2 giá trị : True hoặc False
#Boolean trong toán tử so sánh :
print('Kteam'=="Kteam")
print('Kteam'=='Education')#python so sánh kí tự với nhau bằng các đưa nó về dưới dạng số bằng hàm ord
#Toán tử is
a =[1,2,3]
b =[1,2,3]
print(a==b)# Luôn đúng vì giá trị của nó bằng nhau
print(a is b )#Kq là False vì mặc dù cùng giá trị nhưng nó là 2 đối tượng khác nhau hoàn toàn
a = [1,2,3]
a = b
print(a is b)# Này là true do đang trỏ chung vào 1 địa chỉ thôi
