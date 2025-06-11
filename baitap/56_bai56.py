#Viết hàm truyền vào tham số là chuỗi s và hai số tự nhiên a, b (a <= b). Trả về chuỗi con đảo ngược từ vị trí a đến vị trí b của chuỗi s (vị trí của chuỗi bắt đầu từ 0).
def xuly(s,a,b):
    chuoicon = s[a:b+1]
    chuoicondaonguoc = chuoicon[::-1]
    return chuoicondaonguoc
s = input()
a = int(input())
b = int(input())
print(xuly(s,a,b))
