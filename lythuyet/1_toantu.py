from decimal import*
getcontext().prec = 24
print(Decimal(4)/Decimal(3))
from fractions import*
print(Fraction(3,5))
a = complex(3,4)
print(a)
print(a.real)
print(a.imag)

print(8+3)
print(8-3)
print(8*3)
print(8/3)
print(8//3)# lấy phần nguyên
print(8**3)# 8 mũ 3
print(8%3)#dư của thương

import math
print(math.trunc(3.9))
print(math.floor(3.9))# trả về kết quả < hoặc bằng x
print(math.ceil(3.9))# trả về kết quả > hoặc bằng x
print(math.fabs(-4))
print(math.gcd(3,7))