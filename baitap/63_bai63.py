#Hàm trả về số lượng ký tự nguyên âm và chuỗi s với các ký tự nguyên âm thay thế bằng ký tự "$".
def xuly(s):
    nguyenam = 'ueoaiUEAOI'
    tongnguyenam = 0
    for i in nguyenam :# không dùng range do i phải là ký tự trong nguyenAm chứ kh phải là số
        tongnguyenam += s.count(i) # count đếm số lần xuất hiện của từng kí tự và cộng nó vào trong tongnguyenAm
        s= s.replace(i,'$')
    return tongnguyenam , s
s = input()
soluong , chuois = xuly(s)
print(soluong)
print(chuois)