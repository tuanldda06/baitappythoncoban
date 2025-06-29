#Viết hàm truyền vào tham số là chuỗi s. Hiển thị số lần xuất hiện của các ký tự trong chuỗi s.
def xuly(s):
    for i in s :
        solan = s.count(i)
        print("'{}' :{}".format(i , solan))
s = input()
xuly(s)
#Hàm của bạn hoạt động đúng về mặt đếm số lần xuất hiện ký tự. Tuy nhiên, nó sẽ in trùng nhiều lần nếu ký tự xuất hiện nhiều hơn 1 lần.
#Cách làm tối ưu nhất
def xuly(s) :
    chuoi = ""
    for i in s :
        if i not in chuoi :
            chuoi +=i
    for i in chuoi: 
        print(" '{}': {} ; ".format(i , s.count(i)),end='') # 
s = input()
xuly(s)
#end='' → in xong không xuống dòng.

#end=' ' → in xong xuống dòng bằng 1 dấu cách.

#end='\n' (mặc định) → in xong xuống dòng mới.