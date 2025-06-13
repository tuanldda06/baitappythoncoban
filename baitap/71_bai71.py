#Viết hàm với tham số truyền vào là chuỗi s. Trả về số lượng chữ số, số lượng ký tự, số lượng ký hiệu và chuỗi s được sắp xếp thành ba phần theo thứ tự chữ số, ký tự, ký hiệu.
def xuly(s):
    digit = ""
    chars = ""
    symbol = ""
    for c in s :
        if c.isdigit() :
            digit += c
        elif c.isalpha() :
            chars +=c
        else :
            symbol += c
    thutu = digit +chars + symbol
    return len(digit) ,len(chars) , len(symbol),thutu
s = input()
slkytu, slchuso , slkyhieu , sapxep = xuly(s)
print(slkytu, slchuso , slkyhieu , end = '\n')
print(sapxep)
            