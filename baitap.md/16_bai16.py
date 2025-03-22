#Nhập tên, chiều cao và so sánh chiều cao của hai bạn (Có xử lý ngoại lệ đầu vào)
try :
  ten1 , chieucao1 = input('Nhap lan luot ten va chieu cao ban 1:').split()
  ten2 , chieucao2 = input('Nhap lan luot ten va chieu cao ban 2:').split()
  chieucaoa = int(chieucao1)
  chieucaob = int(chieucao2)
  if chieucaoa<=0 or chieucaob<=0:
    print('chieucao phai lon hon 0')
  elif chieucaoa < chieucaob:
    print(f'{ten1} thap hon {ten2}')
  elif chieucaoa > chieucaob :
    print(f'{ten1} cao hon {ten2}')
  else :
    print(f'{ten1} cao bang {ten2}')
except :
  print('dinh dang dau vao khong hop le!')