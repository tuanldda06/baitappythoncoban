#Nhập tên, chiều cao và so sánh chiều cao của hai bạn
#Định dạng đầu vào :Gồm hai dòng: ,Dòng đầu tiên chứa tên và chiều cao (cm) của bạn thứ nhất, cách nhau bởi khoảng trắng ,Dòng thứ hai chứa tên và chiều cao (cm) của bạn thứ hai, cách nhau bởi khoảng trắng
#Định dạng đầu ra :Gồm một dòng duy nhất hiển thị như sau: {P1} cao hon {P2} ,với {P1} là tên bạn cao hơn, {P2} là tên bạn thấp hơn
ten1 , chieucao1 = input('Nhập lần lượt tên và chiều cao của bạn 1:').split()
ten2 , chieucao2 = input('Nhập lần lượt tên và chiều cao của bạn 2:').split()
chieucaoa = int(chieucao1)
chieucaob = int(chieucao2)
if chieucaoa > chieucaob :
  print(f'{ten1} cao hon {ten2}')
elif chieucaoa < chieucaob:
  print(f'{ten1} thap hon {ten2}')
else :
  print(f'{ten1} cao bang {ten2}')
