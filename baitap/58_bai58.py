#Viết hàm truyền vào tham số là chuỗi s. 
#Trả về chuỗi kết quả bằng cách thay thế đuôi "ing" bằng đuôi "ly" nếu chuỗi s kết thúc bằng "ing", nếu không thì thêm đuôi "ing" vào chuỗi s.
def xuly(s):
    if s[-3:] !='ing' and len(s)<3 :
        return s + 'ing'
    else :
        return s[:-3] +'ly'
s =input()
print(xuly(s))
#Trong s[:-3], Python lấy từ vị trí 0 đến end-1 = -3-1 = -4 (theo chỉ số âm), tức là bỏ 3 ký tự cuối (-3, -2, -1). Điều này khớp với yêu cầu bỏ "ing" trong hàm.
#Còn s[-3:] Số -3 chỉ vị trí bắt đầu, tính ngược từ cuối chuỗi (vị trí cuối là -1, kế cuối là -2, thứ ba từ cuối là -3) còn Dấu : nghĩa là lấy từ vị trí -3 đến hết chuỗi.
#Trong Python, cú pháp lát cắt s[start:end] được sử dụng để lấy một phần của chuỗi (hoặc danh sách, tuple, v.v.) từ vị trí start đến vị trí end-1.

