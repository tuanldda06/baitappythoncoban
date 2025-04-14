try :
    n = int(input())
    for hang in range(n):
        for cot in range(n -hang , stop = 0 ,sep = -1) :
#start = n - hang: Bắt đầu từ giá trị lớn nhất của hàng đó.stop = 0: Dừng lại trước khi đến 0 (tức là in đến 1).step = -1: Lùi từng bước một (đếm lùi).
            print(cot , end = ' ')
        print()
except ValueError :
    print('Dinh dang dau vao khong hop le')
    