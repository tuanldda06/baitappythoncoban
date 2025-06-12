#Viết hàm truyền vào tham số là chuỗi s.
# Nếu ký tự đầu và ký tự cuối của chuỗi s là "*" (hoặc "-") thì  trả về chuỗi s với định dạng title() (hoặc swapcase()). Các trường hợp còn lại trả về chuỗi s với định dạng capitalize().
def xuly(s) :
    if s.startswith('*') and s.endswith('*') :
        return s.title()
    if s.starswith('-') and s.endswith('-') :
        return s.swapcase()
    #startswith('*') và endswith('*'): kiểm tra ký tự đầu/cuối có phải là *.
    return s.capitalize()
s = input()
print(xuly(s))

