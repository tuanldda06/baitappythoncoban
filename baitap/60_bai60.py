#Viết hàm truyền vào tham số là chuỗi s. Nếu ký tự đầu của chuỗi s là ký tự viết thường (hoặc viết hoa) thì trả về chuỗi s với tất cả ký tự được chuyển thành viết thường (hoặc viết hoa). Các trường hợp khác trả về chuỗi s.
def xuly(s): 
    if len(s) == 0 :
        return ' '
    if s[0].islower() :
        return s.lower()
    if s[0].isupper() :
        return s.upper()
    return s
s =input()
print(xuly(s))
#Nếu chuỗi rỗng → trả về chính nó. 
#Nếu ký tự đầu là chữ thường → chuyển cả chuỗi thành chữ thường.
#Nếu ký tự đầu là chữ hoa → chuyển cả chuỗi thành chữ hoa.
#Nếu ký tự đầu không phải chữ cái (ví dụ số, ký tự đặc biệt) → trả về nguyên chuỗi ban đầu.